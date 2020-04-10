import inject
from flask import Flask, jsonify, request


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    number_of_created_goods = db.goods.add_many(request.json)
    return jsonify({'number of items created': number_of_created_goods}), 201


@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    return jsonify(db.goods.get_all())
