from flask_restplus import fields, reqparse
from restplus import api

user_post = api.model ('User post', {
    'name': fields.String(required=True, description='Name of user'),
})

movie_post = api.model ('Movie post', {
    'title': fields.String(required=True, description='Name of movie'),
    'director' : fields.String(required=True, description='Name of director'),
    'ranking' : fields.Float(required=True, description='Ranking of movie',min=1.0,max=10.0)
})

bookings_post = api.model ('Bookings post', {
    'userId' : fields.Integer(required=True, description='User id'),
    'movieIds' : fields.List(fields.String),
    'pubDate' : fields.DateTime,
})

movie_parser = reqparse.RequestParser()
movie_parser.add_argument('title', location='form')
movie_parser.add_argument('director', location='form')
movie_parser.add_argument('ranking', location='form')

booking_parser = reqparse.RequestParser()
booking_parser.add_argument('userId', type=int, location='form')
booking_parser.add_argument('movieIds', action='append', location='form')
booking_parser.add_argument('pubDate', location='form')

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', location='form')
