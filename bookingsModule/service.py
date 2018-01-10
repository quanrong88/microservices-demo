from nameko.rpc import rpc, RpcProxy
import json
from database import engine, metadata, bookings
from serializer import BookingSchema

class BookingsService(object):
    name="bookingsService"
    @rpc
    def hello(self):
        return "hello"

    @rpc
    def list(self):
        command = bookings.select()
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchall()
        schema = BookingSchema(many=True)
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data
    @rpc
    def getByUserId(self, user_id):
        command = bookings.select().where(bookings.c.userId == user_id)
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchall()
        schema = BookingSchema(many=True)
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data
    @rpc
    def getById(self, booking_id):
        command = bookings.select().where(bookings.c.id == booking_id)
        resultsProxy = engine.execute(command)
        results = resultsProxy.fetchone()
        schema = BookingSchema()
        resultDic = schema.dump(results)
        resultsProxy.close()
        return resultDic.data
    @rpc
    def createNewBooking(self, data):
        userIdVal = data.get('userId')
        movieIdsVal = data.get('movieIds')
        pubDateVal = data.get('pubDate')
        movieIdsString = ','.join(map(str, movieIdsVal))
        command = bookings.insert().values(userId=userIdVal,movieIds=movieIdsString,pubDate=pubDateVal)
        resultsProxy = engine.execute(command)
    @rpc
    def deleteBooking(self, booking_id):
        command = bookings.delete().where(bookings.c.id==booking_id)
        resultsProxy = engine.execute(command)
    @rpc
    def updateBooking(self, booking_id, data):
        userIdVal = data.get('userId')
        movieIdsVal = data.get('movieIds')
        pubDateVal = data.get('pubDate')
        movieIdsString = ','.join(map(str, movieIdsVal))
        command = bookings.update().where(bookings.c.id==booking_id).values(userId=userIdVal,movieIds=movieIdsString,pubDate=pubDateVal)
        resultsProxy = engine.execute(command)
