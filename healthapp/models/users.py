#!/usr/bin/python3
""" user model """
from healthapp import db
from healthapp.models.base import BaseModel
from flask_login import UserMixin


class User(BaseModel, db.Model, UserMixin):
    """ user model """
    __tablename__ = 'user'
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
