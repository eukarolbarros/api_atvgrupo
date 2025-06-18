from flask import request, jsonify
from models.message import Message
from db import db

def criar_mensagem():
    data = request.get_json()
    # Força o usuário padrão com ID = 1
    mensagem = Message(conteudo=data['conteudo'], usuario_id=1)
    db.session.add(mensagem)
    db.session.commit()
    return jsonify({"mensagem": "Mensagem criada com sucesso!"}), 201
