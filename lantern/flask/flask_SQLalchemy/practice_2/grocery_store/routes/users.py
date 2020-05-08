import json

from flask import request
from flask_restful import Resource, marshal_with

from grocery_store.models import User
from grocery_store import db
from grocery_store.routes.marshal_structure import users_structure


class Users(Resource):
    @marshal_with(users_structure)
    def get(self):
        return User.query.all()
