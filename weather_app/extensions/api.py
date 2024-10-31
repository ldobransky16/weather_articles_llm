# weather_app/extensions/api.py

from flask_restx import Api

api = Api(
    version='1.0',
    title='Weather API',
    description='API for weather forecasts and article generation',
    doc='/docs'  # Documentation URL
)
