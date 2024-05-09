from flask import Blueprint

from .user import user_blueprint

api = Blueprint('api', __name__)

def init_app(app):
    app.register_blueprint(user_blueprint, url_prefix='/user')