from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    director = fields.Str()
    ranking = fields.Float()
