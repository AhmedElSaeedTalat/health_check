#!/usr/bin/python3
""" user view """
from healthapp.views import user_views
from flask import render_template


@user_views.route('/reg', strict_slashes=False)
def register():
    return render_template('registration.html')
