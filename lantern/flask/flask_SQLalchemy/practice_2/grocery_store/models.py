from grocery_store.db import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    store_id = db.relationship("Store")

    def __repr__(self):
        return f'<id: {self.user_id}, name: {self.name}, email: {self.email}>'


class Good(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    brand = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)


class Store(db.Model):
    __tablename__ = "stores"
    # name, city, address, manager_id
    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

