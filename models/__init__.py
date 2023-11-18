#!/usr/bin/python3

""" initiate sqlalchemy """
from models.engine.db_engine import Engine
new_engine = Engine()
new_engine.reload()
