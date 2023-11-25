#!/usr/bin/python3
""" cmd for the Project """
import cmd
from healthapp import app, db
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
            password = input('password: ')
            email = input('email: ')
            role = 'author'
            pwd = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=pwd,
                        role=role)
            db.session.add(user)
            db.session.commit()
            print('user is created successfully')


if __name__ == "__main__":
    Command().cmdloop()
