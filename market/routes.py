from flask import render_template
from market import app
from market.models import Item


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/store")
def store():
    items = Item.query.all()
    return render_template('store.html', items=items)


@app.route("/store/<int:productId>")
def product(productId):
    return render_template('productPage.html', id=productId)
