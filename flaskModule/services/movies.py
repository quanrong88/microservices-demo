from flask import request
from flask_restplus import Resource
from restplus import api
from nameko.standalone.rpc import ClusterRpcProxy
from serializers import movie_parser
from services import CONFIG

ns = api.namespace('movies/', description='Operations related to movies')

@ns.route('/')
class GetMovies(Resource):
    def get(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            return rpc.moviesService.list()
    @api.expect(movie_parser)
    def post(self):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = movie_parser.parse_args()
            rpc.moviesService.createNewMovies(args)
        return {'message':'Done'}
@ns.route('/<string:movie_id>')
class GetMovieById(Resource):
    def get(self, movie_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            return rpc.moviesService.getMovieById(movie_id)
    @api.expect(movie_parser)
    def put(self, movie_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            args = movie_parser.parse_args()
            rpc.moviesService.updateMovie(movie_id,args)
        return {'message':'Done'}
    def delete(self,movie_id):
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.moviesService.deleteMovie(movie_id)
        return {'message':'Done'}
