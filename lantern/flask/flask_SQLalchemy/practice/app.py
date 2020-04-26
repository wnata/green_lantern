from flask import Flask
from db import db
from config import Config
from users import users


def get_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.register_blueprint(users)
    db.init_app(app)
    return app
