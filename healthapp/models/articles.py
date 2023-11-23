#!/usr/bin/python3
""" article model """
from healthapp import db
from healthapp.models.base import BaseModel


class Article(BaseModel, db.Model):
    """ Article model """
    __tablename__ = 'article'
    title = db.Column(db.String(255), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
