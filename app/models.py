#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-12-10

from hashlib import md5
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, passowrd):
        self.password_hash = generate_password_hash(passowrd)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''The user loader is registered with Flask-Login with the
@login.user_loader decorator. The id that Flask-Login
passes to the function as an argument is going to be a
string, so databases that use numeric IDs need to
convert the string to integer as you see above.'''
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # In this reference the user is the
    # name of the database table, which Flask-SQLAlchemy
    # automatically sets to the name of the model class
    # converted to lowercase.

    def __repr__(self):
        return '<Post {}>'.format(self.body)
