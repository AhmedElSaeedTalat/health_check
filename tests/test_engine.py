#!/usr/bin/python3
""" write test cases """
from healthapp.models.users import User
from flask_wtf.csrf import generate_csrf
from healthapp.views.forms import Registration
from flask import url_for


def test_home(client):
    """ test home page """
    response = client.get('/')
    assert b'<link type="text/css" rel="stylesheet" href="/static/style/main.css">' in response.data


def test_registration(client, app):
    """ test registration function """
    with app.app_context():
        data = {
                'username': 'Jordan',
                'email': 'jordan@mail.com',
                'password': '123456',
                'confirm_password': '123456',
                }
        response = client.post(url_for('user_views.register'), data=data, follow_redirects=True)
        assert response.status_code == 200
        users = User.query.all()
        assert len(users) == 1
        user = User.query.first()
        assert user.email == 'jordan@mail.com'
