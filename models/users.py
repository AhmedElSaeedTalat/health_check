#!/usr/bin/python3
""" user model """
from models.base import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ user model """
    __tablename__ = 'users'
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, username, email, password):
        """ init user model """
        self.username = username
        self.email = email
        self.password = password
