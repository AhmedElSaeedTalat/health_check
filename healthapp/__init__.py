#!/usr/bin/python3
from flask import Flask, render_template
from healthapp.views.users import user_views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
usr = os.getenv('username')
pwd = os.getenv('pwd')
host = os.getenv('host')
dbEnv = os.getenv('db')


app = Flask(__name__)
app.register_blueprint(user_views)
url = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, dbEnv)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '9911a688421666c9f6938371a154c590b86459a2aeb01eda'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from healthapp.models.users import User
    return User.query.get(int(user_id))


@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('notfound.html')
