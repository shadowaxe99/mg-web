from flask import Blueprint
from .routes import conversation_routes, features_routes, monetization_routes

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Registering the routes from the routes.py file
api_blueprint.register_blueprint(conversation_routes, url_prefix='/conversation')
api_blueprint.register_blueprint(features_routes, url_prefix='/features')
api_blueprint.register_blueprint(monetization_routes, url_prefix='/monetization')