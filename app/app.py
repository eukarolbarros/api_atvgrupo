from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.controllers.user_controller import usuario_bp
from app.controllers.message_controller import mensagem_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models.user import Usuario
from app.models.message import Mensagem

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()  

    # Registrar blueprints
    from app.controllers.user_controller import usuario_bp
    from app.controllers.message_controller import mensagem_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensagem_bp)

    return app
if __name__ == '__main__':
    app.run(debug=True)
