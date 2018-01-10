from flask import request
from flask_restplus import Resource, reqparse
from restplus import api
from nameko.standalone.rpc import ClusterRpcProxy
from serializers import user_parser
from services import CONFIG

ns = api.namespace('user/', description='Operations related to user')

@ns.route('/')
class showListUsers(Resource):
    def get(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            return rpc.userService.list()
    @api.expect(user_parser)
    def post(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = user_parser.parse_args()
            rpc.userService.createNewUser(args)
        return {'message':'Done'}

@ns.route('/<int:user_id>')
class showUser(Resource):
    def get(self,user_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            return rpc.userService.getUserByName(user_id)
    @api.expect(user_parser)
    def put(self,user_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = user_parser.parse_args()
            rpc.userService.updateUser(user_id, args)
        return {'message':'Done'}
    def delete(self, user_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.userService.deleteUser(user_id)
        return {'message':'Done'}
@ns.route('/<string:user_id>/Bookings/')
class showBookingsForUsername(Resource):
    def get(self,user_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            userBookings = rpc.bookingsService.getByUserId(user_id)
            results = []
            for bookingDic in userBookings:
                tempDic = {}
                tempDic['id']=bookingDic['id']
                tempDic['pubDate']=bookingDic['pubDate']
                moviesList = []
                for movieId in bookingDic['movieIdsList']:
                    movieDic = rpc.moviesService.getMovieById(movieId)
                    if(bool(movieDic)):
                        moviesList.append(movieDic)
                tempDic['movies'] = moviesList
                results.append(tempDic)
            return results

# @ns.route('/hello')
# class hello(Resource):
#     @api.expect(user_parser)
#     def post(self):
#         args = user_parser.parse_args()
#         return args
