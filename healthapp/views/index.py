#!/usr/bin/python3
""" main file """
from flask import render_template, jsonify
from healthapp.views.forms import SearchForm
from healthapp.views.drugsView import medicine_views 



def home():
    """ home view function """
    return render_template('index.html')
