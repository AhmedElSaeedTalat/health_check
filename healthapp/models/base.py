#!/usr/bin/python3
""" base model """
from healthapp import db
from datetime import datetime


class BaseModel:
    """ base model """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self):
        pass
