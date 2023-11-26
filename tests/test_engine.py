#!/usr/bin/python3
""" write test cases """
from healthapp.models.users import User
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
        response = client.post(url_for('user_views.register'), data=data,
                               follow_redirects=True)
        assert response.status_code == 200
        users = User.query.all()
        assert len(users) == 1
        user = User.query.first()
        assert user.email == 'jordan@mail.com'
        assert b'<li>Jordan</li>' in response.data


def test_login(client, app):
    """
        function to test login process
        -- first registration is made
        -- second logout is made
        -- third login is made
    """
    with app.app_context():
        data = {
                'username': 'Jordan',
                'email': 'jordan@mail.com',
                'password': '123456',
                'confirm_password': '123456',
                }
        client.post(url_for('user_views.register'), data=data,
                    follow_redirects=True)
        client.get(url_for('user_views.logout'), follow_redirects=True)
        data = {
                'email': 'jordan@mail.com',
                'password': '123456',
                }
        response = client.post(url_for('user_views.login'), data=data,
                               follow_redirects=True)
        assert response.status_code == 200
        assert b'<li>Jordan</li>' in response.data


def test_search(client, app):
    """ test search form """
    with app.app_context():
        data = {'name': 'Zoloft'}
        response = client.post(url_for('medicine_views.display_med'),
                               data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b'<h4>description</h4>' in response.data
