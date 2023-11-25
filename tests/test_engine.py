#!/usr/bin/python3
""" write test cases """


def test_home(client):
    """ test home page """
    response = client.get('/')
    assert b'<link type="text/css" rel="stylesheet" href="/static/style/main.css">' in response.data
