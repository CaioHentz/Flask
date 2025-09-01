from flask import Flask
from .Hello.routes import hello_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)

    return app
