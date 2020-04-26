import csv
from flask import Flask
from sqlalchemy_utils import create_database, drop_database, database_exists

from db import db
from models import User, Store, Good
from config import Config


def configure_db():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    app.app_context().push()
    print("Database configured!")


def create_db():
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
        # create all tables
        db.create_all()
        print('Database successfully created!')
    else:
        print('Database already exists!')


def delete_db():
    if database_exists(db.engine.url):
        drop_database(db.engine.url)
        print('Database successfully dropped!')


def populate_users():
    with open('users.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.session.add(User(**row))
    db.session.commit()


def populate_stores():
    with open('stores.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.session.add(Store(**row))
    db.session.commit()


def populate_goods():
    with open('goods.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.session.add(Good(**row))
    db.session.commit()


# configure_db()
# create_db()
