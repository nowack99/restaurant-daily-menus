from flask import Blueprint

# Import the blueprints
from .restaurant_routes import restaurant_routes
from .menu_routes import menu_routes

# main blueprint
routes_blueprint = Blueprint('routes', __name__)

# Register of blueprints
routes_blueprint.register_blueprint(restaurant_routes)
routes_blueprint.register_blueprint(menu_routes)
