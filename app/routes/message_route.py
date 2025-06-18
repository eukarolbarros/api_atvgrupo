from flask import Blueprint
from controllers.message_controller import criar_mensagem

message_bp = Blueprint('mensagem', __name__)
message_bp.route('/', methods=['POST'])(criar_mensagem)
