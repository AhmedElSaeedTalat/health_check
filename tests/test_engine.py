#!/usr/bin/python3
""" module for tests """
import pytest
import os
from healthapp import app, db
from healthapp.models.users import User
from healthapp.models.drugs import Drug
from healthapp.models.articles import Article
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import generate_csrf


@pytest.fixture()
def app():
    app = 








class TestModels(unittest.TestCase):
    """ test models class """
    def setUp(self):
        """ setup db """
        usr = os.getenv('username')
        pwd = os.getenv('pwd')
        host = os.getenv('host')
        dbEnv = os.getenv('db')
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, dbEnv)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = url
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """ drop tables after each test """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_users(self):
        """ test creating registeration """
        with self.app_context as context:
            with context.test_request_context():
                with self.app as client:
                    with client.session_transaction():
                        csrf_token = generate_csrf()
                    data = {
                            'user_name': 'James',
                            'email': 'james@mail.com',
                            'password': '123456',
                            'confirm_password': '123456',
                            'csrf_token': csrf_token
                            }
                    response = client.post('/reg', data=data, follow_redirects=True)
                    self.assertEqual(response.status_code, 200)

