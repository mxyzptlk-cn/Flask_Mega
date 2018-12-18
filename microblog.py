#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}