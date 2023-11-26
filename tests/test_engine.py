#!/usr/bin/python3
""" write test cases """
from healthapp.models.users import User
from healthapp.models.drugs import Drug
from flask import url_for
from flask import jsonify
import json


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
        assert b"<button class='btn save_drug'>save drug</button>" not in response.data


def test_saveDrug(client, app):
    """ test save drug function """
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
        client.post(url_for('user_views.login'), data=data,
                    follow_redirects=True)
        data = {'name': 'Zoloft'}
        response = client.post(url_for('medicine_views.display_med'),
                               data=data, follow_redirects=True)
        assert b"<button class='btn save_drug'>save drug</button>" in response.data

        """ test clicking save drug to save drug """
        data = 'Zoloft'
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = client.post(url_for('medicine_views.save_drug'),
                               headers=headers,
                               data=data,
                               follow_redirects=True)
        count = Drug.query.count()
        drug = Drug.query.filter_by(name='Zoloft').first()
        user = drug.user
        assert user[0].id == 1
        assert response.status_code == 200
        assert count == 1


def test_display_symptoms(client, app):
    """ test retrieving symptoms form"""
    with app.app_context():
        response = client.get(url_for('medicine_views.health_check'),
                              follow_redirects=True)
        assert response.status_code == 200
        assert b'<label for="select_options">please select your symptoms</label>' in response.data
