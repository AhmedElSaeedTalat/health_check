#!/usr/bin/python3
""" module for tests """
import pytest
from healthapp import create_app, db
from healthapp.models.users import User
from healthapp.models.drugs import Drug
from healthapp.models.articles import Article
import os


@pytest.fixture()
def app():
    """ setting up the app for testing """
    app = create_app()
    with app.app_context():
        db.create_all()
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SERVER_NAME'] = 'localhost'
        app.config['TESTING'] = True
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    """ function to simulate requests """
    return app.test_client()
