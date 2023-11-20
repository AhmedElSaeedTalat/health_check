#!/usr/bin/python3
from flask import Flask, render_template
from healthapp.views.users import user_views
from healthapp.views.drugsView import medicine_views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from healthapp.views import index
from flask_session import Session
import os
usr = os.getenv('username')
pwd = os.getenv('pwd')
host = os.getenv('host')
dbEnv = os.getenv('db')


app = Flask(__name__)
app.register_blueprint(user_views)
app.register_blueprint(medicine_views)
url = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, dbEnv)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '9911a688421666c9f6938371a154c590b86459a2aeb01eda'
app.config['SESSION_TYPE'] = 'redis'
Session(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


app.add_url_rule('/', view_func=index.home)


@app.context_processor
def inject_variable():
    """ add form before templates get rendered """
    from healthapp.views.forms import SearchForm
    searchform = SearchForm()
    return {'searchform': searchform}


@login_manager.user_loader
def load_user(user_id):
    from healthapp.models.users import User
    return User.query.get(int(user_id))


@app.errorhandler(404)
def not_found(e):
    return render_template('notfound.html')
