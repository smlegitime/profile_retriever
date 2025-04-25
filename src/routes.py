from flask import Blueprint
from src.controllers.profile_controller import profiles

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(profiles, url_prefix="/profiles")