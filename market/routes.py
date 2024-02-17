from flask import render_template, redirect, url_for
from market import app, db
from market.models import Item, User
from market.forms import RegisterForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/store")
def store():
    items = Item.query.all()
    return render_template('store.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('store'))
    return render_template('register.html', form=form)

# @app.route("/store/<int:productId>")
# def product(productId):
#     return render_template('productPage.html', id=productId)
