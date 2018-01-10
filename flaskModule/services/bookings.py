from flask import request
from flask_restplus import Resource
from restplus import api
from nameko.standalone.rpc import ClusterRpcProxy
from serializers import booking_parser
from services import CONFIG

ns = api.namespace('bookings/', description='Operations related to bookings')

@ns.route('/')
class GetBookings(Resource):
    def get(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            return rpc.bookingsService.list()
    @api.expect(booking_parser)
    def post(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = booking_parser.parse_args()
            rpc.bookingsService.createNewBooking(args)
        return {'message':'Done'}
@ns.route('/<string:booking_id>')
class GetBookingsForUsername(Resource):
    def get(self, booking_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            bookingsDic = rpc.bookingsService.getById(booking_id)
            result = {}
            result['id'] = bookingsDic['id']
            result['pubDate'] = bookingsDic['pubDate']
            moviesList = []
            for movieId in bookingsDic['movieIdsList']:
                movieDic = rpc.moviesService.getMovieById(movieId)
                if(bool(movieDic)):
                    moviesList.append(movieDic)
            result['movies'] = moviesList
            result['user'] = rpc.userService.getUserByName(bookingsDic['userId'])
            return result
    @api.expect(booking_parser)
    def put(self, booking_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = booking_parser.parse_args()
            rpc.bookingsService.updateBooking(booking_id, args)
        return {'message':'Done'}
    def delete(self, booking_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.bookingsService.deleteBooking(booking_id)
        return {'message':'Done'}
