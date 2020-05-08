from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from grocery_store.config import Config


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

def make_db(app):
    db = SQLAlchemy()
    db.init_app(app)
    return db
