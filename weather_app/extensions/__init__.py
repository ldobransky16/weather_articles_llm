# weather_app/extensions/__init__.py
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()
api = Api(version='1.0', title='Weather API', description='API for weather forecasts and article generation')
