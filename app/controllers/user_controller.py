from flask import request, jsonify
from models.user import User
from db import db

def criar_usuario():
    data = request.get_json()
    try:
        usuario = User(**data)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
