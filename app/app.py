from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from .views.cars import cars_bp


def setup_swagger(app):
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swagger_bp = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Lecture12_Example1"
        }
    )
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)


def create_app():
    app = Flask(__name__)
    setup_swagger(app)
    app.register_blueprint(cars_bp)
    return app
