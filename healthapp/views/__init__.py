#!/usr/bin/python3
from flask import Blueprint

user_views = Blueprint('user_views', __name__, url_prefix='/user')
from healthapp.views.users import *
