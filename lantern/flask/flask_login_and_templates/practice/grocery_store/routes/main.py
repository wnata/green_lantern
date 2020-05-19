from flask import Blueprint, render_template
from flask_login import current_user
from grocery_store.models import Good
from grocery_store.database import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)


@main.route('/goods-page')
def goods_page():
    goods = Good.query.all()
    return render_template('goods.html', goods=goods)
