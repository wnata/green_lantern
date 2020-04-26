from flask_restful import fields


user_structure = {
    "user_id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String,
}
