from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    with app.app_context():
        db = init_db()
        db = SQLAlchemy()
        db.init_app(app)
        db.create_all()
        db.session.commit()
