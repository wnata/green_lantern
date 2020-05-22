from flask import Blueprint, render_template
from grocery_store.database import db
from grocery_store.models import User, Store, Good, Order, OrderLine
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)


@main.route('/orders')
@login_required
def orders():
    orders = Order.query.filter(Order.user_id==current_user.user_id).all()
    orders_list = [] # takes {id:1, body:{store:name, goods:[1,2,3]}}
    for order in orders:
        order_dict = {}

        body_dict = {}
        store = Store.query.filter(Store.store_id==order.store_id).first()
        body_dict['store_name']= store.name

        order_lines = OrderLine.query.filter(order.order_id == OrderLine.order_id).all()
        goods = []
        for order_line in order_lines:
            good = Good.query.filter(Good.good_id==order_line.good_id).first()
            goods.append(good.name)

        body_dict['goods'] = goods

        order_dict[order.order_id] = body_dict
        orders_list.append(order_dict)

    return render_template('orders.html', orders=orders_list)