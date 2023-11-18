#!/usr/bin/python3
from models.users import User
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class Engine:
    __engine = None
    __session = None

    def __init__(self):
        """ function to connect to db """
        usr = os.getenv('username')
        pwd = os.getenv('pwd')
        host = os.getenv('host')
        db = os.getenv('db')
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)

    def reload(self):
        """ migrate models, creates tables, and start session """
        Base.metadata.create_all(bind=self.__engine)
        session_creation = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_creation)
        self.__session = Session()

    def save(self, obj):
        """ create new object and insert in db """
        self.__session.add(obj)
        self.__session.commit()
