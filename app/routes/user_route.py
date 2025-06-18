from flask import Blueprint
from controllers.user_controller import criar_usuario

user_bp = Blueprint('usuario', __name__)
user_bp.route('/', methods=['POST'])(criar_usuario)
