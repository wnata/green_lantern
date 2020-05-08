from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from grocery_store.config import Config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
