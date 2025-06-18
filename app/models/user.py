from db import db
from sqlalchemy.orm import validates
import re

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    mensagens = db.relationship('Message', backref='usuario', lazy=True)

    @validates('email')
    def validate_email(self, key, email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(padrao, email):
            raise ValueError("Email inválido")
        return email

    @validates('nome')
    def validate_nome(self, key, nome):
        if not nome or nome.strip() == '':
            raise ValueError("Nome não pode ser vazio")
        return nome

    @validates('senha')
    def validate_senha(self, key, senha):
        if len(senha) < 8:
            raise ValueError("Senha deve ter pelo menos 8 caracteres")
        if not re.search(r'[A-Z]', senha):
            raise ValueError("Senha deve conter pelo menos uma letra maiúscula")
        if not re.search(r'[a-z]', senha):
            raise ValueError("Senha deve conter pelo menos uma letra minúscula")
        if not re.search(r'\d', senha):
            raise ValueError("Senha deve conter pelo menos um dígito")
        if not re.search(r'[@!%*?]', senha):
            raise ValueError("Senha deve conter pelo menos um caractere especial (@!%*?)")
        return senha

