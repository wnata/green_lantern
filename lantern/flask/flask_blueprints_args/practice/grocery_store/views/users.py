from flask import Blueprint
import inject

users = Blueprint('users', __name__)


@users.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@users.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@users.route('/')
def get_method():
    return "Hello from module 1"
