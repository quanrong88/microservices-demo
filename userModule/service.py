from nameko.rpc import rpc, RpcProxy
import json
from database import engine, metadata, users
from serializer import UserSchema

class UserService(object):
    name = "userService"


    @rpc
    def list(self):
        command = users.select()
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchall()
        schema = UserSchema(many=True)
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data

    @rpc
    def getUserByName(self, user_id):
        command = users.select().where(users.c.id == user_id)
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchone()
        schema = UserSchema()
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data

    @rpc
    def createNewUser(self, data):
        username = data.get('name')
        command = users.insert().values(name=username)
        resultsProxy = engine.execute(command)

    @rpc
    def deleteUser(self,user_id):
        command = users.delete().where(users.c.id==user_id)
        resultsProxy = engine.execute(command)

    @rpc
    def updateUser(self,user_id, data):
        username = data.get('name')
        command = users.update().where(users.c.id==user_id).values(name=username)
        resultsProxy = engine.execute(command)
