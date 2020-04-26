from flask import request
from flask_restful import Resource, marshal_with

from db import db

from users.marshal_structure import user_structure
from models import User
import json


class UsersRoutes(Resource):
    @marshal_with(user_structure)
    def get(self, user_id=None):
        if user_id:
            data = User.query.get(user_id)
            return data
        return User.query.all()

    # def post(self):
    #     data = json.loads(request.data)
    #     new_post = NewsModel(**data)
    #     db.session.add(new_post)
    #     db.session.commit()
    #     return "Successfully added a new news"

    # def put(self, value):
    #     data = json.loads(request.data)
    #     post = NewsModel.query.get(value)

    #     post.title = data.get("title")
    #     post.text = data.get("text")

    #     db.session.commit()
    #     return "Successfully updated the value"

    # def delete(self, value):
    #     post = NewsModel.query.get(value)
    #     db.session.delete(post)
    #     db.session.commit()
    #     return "Successfully deleted the value"
