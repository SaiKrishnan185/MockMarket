from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '5e909070b9cd6954a46fc3e2'
app.app_context().push()
db = SQLAlchemy(app)

from market import routes
