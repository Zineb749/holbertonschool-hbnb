from flask import Blueprint
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns 

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Création de l'instance de l'API Flask-RESTx
    api = Api(api_bp, title='HBnB API', version='1.0', description='API for HBnB')
    api.add_namespace(users_ns, path='/users')
    api.add_namespace(amenities_ns, path='/amenities')
    return app
