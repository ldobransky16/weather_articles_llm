# weather_app/schemas.py

from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime

def validate_latitude(value):
    if not -90 <= value <= 90:
        raise ValidationError('Latitude must be between -90 and 90 degrees.')

def validate_longitude(value):
    if not -180 <= value <= 180:
        raise ValidationError('Longitude must be between -180 and 180 degrees.')

class WeatherArticleRequestSchema(Schema):
    latitude = fields.Float(required=True, validate=validate_latitude)
    longitude = fields.Float(required=True, validate=validate_longitude)
    date = fields.Date(format='%Y-%m-%d', required=True)
    language = fields.Str(validate=validate.OneOf(['en', 'sk']), missing='en')
