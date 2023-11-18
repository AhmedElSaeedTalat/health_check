#!/usr/bin/python3
""" base model """
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """ base model """
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self):
        pass

    def save(self):
        """ create new object and save in db"""
        import models
        models.new_engine.save(self)
