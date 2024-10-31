from flask_swagger_ui import get_swaggerui_blueprint

def init_app(app):
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'  # Place swagger.yaml in the static directory

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Weather API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
