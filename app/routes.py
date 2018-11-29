#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask.'
