from flask import Flask
from grocery_store.config import Config
from grocery_store.db import db
from grocery_store.routes import users, goods, stores


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(goods)
    app.register_blueprint(stores)
    return app


def make_db(app):
    db.init_app(app)
    return db
