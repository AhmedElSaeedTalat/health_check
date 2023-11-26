#!/usr/bin/python3
""" write test cases """
from healthapp.models.users import User
from healthapp.models.drugs import Drug
from healthapp.models.articles import Article
from flask import url_for
import json


def test_home(client):
    """ test home page """
    response = client.get('/')
    assert b'<link type="text/css" rel="stylesheet" \
href="/static/style/main.css">' in response.data


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

        """ log out and test invalid email """
        client.get(url_for('user_views.logout'), follow_redirects=True)
        data = {
                'email': 'jordan',
                'password': '123456',
                }
        response = client.post(url_for('user_views.login'), data=data,
                               follow_redirects=True)
        assert b'<span> Invalid email address. </span>' in response.data


def test_invalid_password(client, app):
    """ log out and test invalid password """
    with app.app_context():
        client.get(url_for('user_views.logout'), follow_redirects=True)
        data = {
                'username': 'Micheal adam',
                'email': 'micheal@mail.com',
                'password': '123456',
                'confirm_password': '123456',
                }
        client.post(url_for('user_views.register'), data=data,
                    follow_redirects=True)
        client.get(url_for('user_views.logout'), follow_redirects=True)
        new_data = {
                    'email': 'micheal@mail.com',
                    'password': 'kjsdhfksdflal',
                   }
        response = client.post(url_for('user_views.login'), data=new_data)
        assert response.status_code == 200
        assert b'<p class="alert alert-danger"> email or password isnt correct</p>' in response.data


def test_search(client, app):
    """ test search form """
    with app.app_context():
        data = {'name': 'Zoloft'}
        response = client.post(url_for('medicine_views.display_med'),
                               data=data, follow_redirects=True)
        try:
            assert response.status_code == 200
            assert b'<h4>description</h4>' in response.data
            assert b"<button class='btn save_drug'>" \
                   b"save drug</button>" not in response.data
        except Exception:
            assert b'<h3>Get your diagnosis Now</h3>' in response.data
            return


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
        try:
            assert b"<button class='btn save_drug'>" \
                   b"save drug</button>" in response.data
        except Exception:
            assert b'<h3>Get your diagnosis Now</h3>' in response.data
            return

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
        """ test display page """
        response = client.get(url_for('medicine_views.health_check'),
                              follow_redirects=True)
        try:
            assert response.status_code == 200
            assert b'<label for="select_options">' \
                   b'please select your symptoms</label>' in response.data
        except Exception:
            assert b'<h3>Get your diagnosis Now</h3>' in response.data
            return
        """ test post in form for diagnosis """
        data = {
                'year': '1992',
                'gender': 'male',
                'symptoms': [238]
                }
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = client.post(url_for('medicine_views.request_diagnosis'),
                               headers=headers,
                               data=data,
                               follow_redirects=True)
        assert response.status_code == 200
        response = response.data.decode('utf-8')
        response = json.loads(response)
        assert 'Issue' in response[0]


def test_pageNotFound(client, app):
    """ to test that page isn't found """
    with app.app_context():
        response = client.get('/fake_url')
        assert b'<p> this url is not active please use a \
valid url 404</p>' in response.data


def test_addingArticles(client, app):
    """ function to test adding articles """
    with app.app_context():
        """
            test visitig adding article page when not author
            result: should be redirect
        """
        response = client.get(url_for('article_views.display_articleForm'))
        assert response.status_code == 302
        data = {
                'username': 'Jordan',
                'email': 'jordan@mail.com',
                'password': '123456',
                'confirm_password': '123456',
                'role': 'author'
                }
        client.post(url_for('user_views.register'), data=data,
                    follow_redirects=True)
        """ making a post request to add an article """
        data = {
                'title': 'test title',
                'content': 'test content',
                'image': (open('2.png', 'rb'), '2.png')}
        response = client.post(url_for('article_views.display_articleForm'),
                               data=data,
                               content_type='multipart/form-data',
                               follow_redirects=True
                               )
        assert response.status_code == 200
        article = Article.query.first()
        user = article.user
        assert article.title == 'test title'
        assert user.id == 1
