# weather_app/routes/weather_article.py

from flask_restx import Namespace, Resource, fields
from flask import request
from marshmallow import ValidationError
from weather_app.services.weather_article_service import generate_weather_article
from weather_app.schemas import WeatherArticleRequestSchema

# Create a namespace for the weather article endpoint
ns = Namespace('weather_article', description='Generate weather articles based on location and mode')

# Define the response models
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
    'error': fields.String,
    'details': fields.Raw
})

@ns.route('/')
class WeatherArticle(Resource):
    # method_decorators = [require_api_key]

    @ns.marshal_with(weather_article_response_model, code=200, description='Success', skip_none=False)
    def get(self):
        """
        Generate a weather article based on location and response mode.
        """
        args = request.args
        schema = WeatherArticleRequestSchema()
        try:
            data = schema.load(args)
        except ValidationError as err:
            ns.abort(400, error='Validation Error', details=err.messages)

        latitude = data['latitude']
        longitude = data['longitude']
        language = data.get('language', 'en')
        date = data.get('date', None)

        result, status_code = generate_weather_article(latitude, longitude, date, language)
        if status_code != 200:
            ns.abort(status_code, **result)
        return result, 200
