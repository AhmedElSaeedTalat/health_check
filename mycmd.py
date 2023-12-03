#!/usr/bin/python3
""" cmd for the Project """
import cmd
from healthapp import db
from healthapp.runapp import app
from healthapp.models.users import User
from flask_bcrypt import Bcrypt


class Command(cmd.Cmd):
    """ class for cmd """
    prompt = '$ '

    def do_quit(self, line):
        """ command to quit CMD """
        return True

    def do_EOF(self, line):
        """ to quit """
        print()
        return True

    def do_create_author(self, line):
        """ function to create author"""
        with app.app_context():
            bcrypt = Bcrypt()
            username = input('username: ')
            user = User.query.filter_by(username=username).first()
            while user:
                print('username exists please choose another one')
                username = input('username: ')
                user = User.query.filter_by(username=username).first()
            password = input('password: ')
            email = input('email: ')
            user = User.query.filter_by(email=email).first()
            while user:
                print('email exists please choose another one')
                email = input('email: ')
                user = User.query.filter_by(email=email).first()
            role = 'author'
            pwd = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=pwd,
                        role=role)
            db.session.add(user)
            db.session.commit()
            print('user is created successfully')


if __name__ == "__main__":
    Command().cmdloop()
