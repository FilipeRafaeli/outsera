import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import models, routes, utils
        db.create_all()
        base_dir = os.path.abspath(os.path.dirname(__file__))
        arquivo = os.path.join(base_dir, 'assets', 'Movielist.csv')

        utils.carregar_csv(arquivo)

    app.register_blueprint(routes.app)

    return app
