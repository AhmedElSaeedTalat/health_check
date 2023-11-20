#!/usr/bin/python3
from healthapp import app, db
from healthapp.models.users import User
from healthapp.models.drugs import Drug
with app.app_context():
    db.create_all()
