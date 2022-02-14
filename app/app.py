from flask import Flask

from .views.cars import cars_bp


def create_app():
    app = Flask(__name__)
    # app.config["SERVER_NAME"] = "127.0.0.1:5000"
    app.config['FLASK_DEBUG'] = 1
    app.register_blueprint(cars_bp)
    return app
