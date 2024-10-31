# weather_app/routes/weather_article.py

from flask_restx import Namespace, Resource, fields
from flask import request
from marshmallow import ValidationError

ns = Namespace('weather_article', description='Generate weather articles based on location and mode')

# Define the response model
coordinates_model = ns.model('Coordinates', {
    'latitude': fields.Float,
    'longitude': fields.Float
})

location_model = ns.model('Location', {
    'name': fields.String,
    'country': fields.String,
    'coordinates': fields.Nested(coordinates_model)
})

weather_model = ns.model('Weather', {
    'description': fields.String,
    'temperature': fields.Float,
    'humidity': fields.Integer,
    'wind_speed': fields.Float
})
mode_model = ns.model('Mode', {
    'headline': fields.String,
    'lead': fields.String,
    'body': fields.String
})

article_model = ns.model('Article', {
    'catastrophic': fields.Nested(mode_model),
    'sensational': fields.Nested(mode_model)
})

weather_article_response_model = ns.model('WeatherArticleResponse', {
    'location': fields.Nested(location_model),
    'weather': fields.Nested(weather_model),
    'article': fields.Nested(article_model)
})

error_model = ns.model('Error', {
    'error': fields.String
})
