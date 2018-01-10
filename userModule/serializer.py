from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
