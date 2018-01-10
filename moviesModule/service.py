from nameko.rpc import rpc, RpcProxy
import json
from database import engine, metadata, movies
from serializer import MovieSchema

class MoviesService(object):
    name="moviesService"

    @rpc
    def list(self):
        command = movies.select()
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchall()
        schema = MovieSchema(many=True)
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data
    @rpc
    def getMovieById(self,movie_id):
        command = movies.select().where(movies.c.id == movie_id)
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchone()
        schema = MovieSchema()
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data
    @rpc
    def createNewMovies(self,data):
        titleVal = data.get('title')
        directorVal = data.get('director')
        rankingVal = data.get('ranking')
        command = movies.insert().values(title=titleVal,director=directorVal,ranking=rankingVal)
        resultsProxy = engine.execute(command)
    @rpc
    def deleteMovie(self,movie_id):
        command = movies.delete().where(movies.c.id==movie_id)
        resultsProxy = engine.execute(command)
    @rpc
    def updateMovie(self,movie_id, data):
        titleVal = data.get('title')
        directorVal = data.get('director')
        rankingVal = data.get('ranking')
        command = movies.update().where(movies.c.id==movie_id).values(title=titleVal,director=directorVal,ranking=rankingVal)
        resultsProxy = engine.execute(command)
