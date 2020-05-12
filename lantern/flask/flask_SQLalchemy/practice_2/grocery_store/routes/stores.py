from flask_restful import Resource, marshal

from grocery_store.models import Store
from grocery_store.routes.marshal_structure import stores_structure


class Stores(Resource):
    def get(self, good_id=None):
        if good_id:
            good = Store.query.get(good_id)
            if good:
                return marshal(good, stores_structure)
            return f"No such good with id: {good_id}"
        return marshal(Store.query.all(), stores_structure)
