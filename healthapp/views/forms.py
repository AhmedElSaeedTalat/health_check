#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.validators import ValidationError


class Registration(FlaskForm):
    """ registration form class """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        from healthapp.models.users import User
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username exists, please use another user')

    def validate_email(self, email):
        from healthapp.models.users import User
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email exists, please use another email')


class Login(FlaskForm):
    """ registration form class """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-in')
