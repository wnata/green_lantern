import csv

from sqlalchemy_utils import create_database, drop_database, database_exists

from app import get_app
from db import db
from models import User, Store, Good


app = get_app()

def create_db():
    with app.app_context():
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
            # create all tables
            db.create_all()
            print('Database successfully created!')
        else:
            print('Database already exists!')


def delete_db():
    with app.app_context():
        if database_exists(db.engine.url):
            drop_database(db.engine.url)
            print('Database successfully dropped!')


def populate_users():
    with open('users.csv') as f, app.app_context():
        reader = csv.DictReader(f)
        for user in reader:
            db.session.add(User(**user))
        db.session.commit()


def populate_stores():
    with open('stores.csv') as f, app.app_context():
        reader = csv.DictReader(f)
        for store in reader:
            db.session.add(Store(**store))
        db.session.commit()


def populate_goods():
    with open('goods.csv') as f, app.app_context():
        reader = csv.DictReader(f)
        for row in reader:
            db.session.add(Good(**row))
        db.session.commit()
