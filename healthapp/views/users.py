#!/usr/bin/python3
""" user view """
from healthapp.views.forms import Registration
from healthapp.views.forms import Login
from flask import render_template, redirect, url_for
from flask_bcrypt import Bcrypt
from flask import Blueprint
from flask_login import login_user, current_user, logout_user

user_views = Blueprint('user_views', __name__, url_prefix='/user')
bcrypt = Bcrypt()


@user_views.route('/reg', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user_views.profile'))
    form = Registration()
    if form.validate_on_submit():
        from healthapp import db
        from healthapp.models.users import User
        pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=pwd)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('user_views.profile'))
    return render_template('registration.html', form=form)


@user_views.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user_views.profile'))
    from healthapp.models.users import User
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user)
            return redirect(url_for('user_views.profile'))
    return render_template('login.html', form=form)


@user_views.route('/user', strict_slashes=False)
def profile():
    return render_template('user.html')


@user_views.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('home'))