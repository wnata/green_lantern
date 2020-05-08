import json

from flask import request
from flask_restful import Resource, marshal_with

from grocery_store.models import User
from grocery_store import db


class Users(Resource):
    def get(self):
        return User.query.all()
