from flask import Flask
from app.routes.main_routes import main_routes
from app.routes.assistant_routes import assistant_routes

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(assistant_routes)

    return app
