from marshmallow import Schema, fields

class ListField(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return []
        return value.split(",")

class BookingSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    userId = fields.Integer()
    pubDate = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    movieIdsList = ListField(attribute="movieIds")
