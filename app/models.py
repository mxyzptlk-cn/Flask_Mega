#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-12-10

from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


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
