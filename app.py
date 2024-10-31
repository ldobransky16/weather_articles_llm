# app.py
from flask import Flask
from flask_migrate import Migrate
from weather_app.extensions import db, api, swagger
from weather_app.routes.weather_article import ns as weather_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    migrate = Migrate(app, db)
    db.init_app(app)
    api.init_app(app)
    swagger.init_app(app)
    api.add_namespace(weather_ns)
    return app
