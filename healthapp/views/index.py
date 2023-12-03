#!/usr/bin/python3
""" main file """
from flask import render_template


def main():
    """ show landing page """
    return render_template('about.html')


def home():
    """ home view function """
    from healthapp.models.articles import Article
    articles = Article.query.order_by(Article.created_at.desc()).limit(2).all()
    return render_template('index.html', articles=articles)
