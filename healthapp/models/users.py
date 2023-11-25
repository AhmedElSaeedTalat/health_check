#!/usr/bin/python3
""" user model """
from healthapp import db
from healthapp.models.base import BaseModel
from flask_login import UserMixin
from healthapp.models.drugs import users_drugs
from healthapp.models.articles import Article


class User(BaseModel, db.Model, UserMixin):
    """ user model """
    __tablename__ = 'user'
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(150), default='client')
    drug = db.relationship('Drug', secondary=users_drugs,
                           back_populates="user")
    article = db.relationship('Article', backref='user')

    def __init__(self, username, email, password, role=""):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
