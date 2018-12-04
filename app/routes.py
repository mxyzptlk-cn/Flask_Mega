#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lex'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautify day in Portland.'
        },
        {
            'author': {'username': 'Lex'},
            'body': 'The brown fox jumps over the lazy dog.'
        },
        {
            'author': {'username': 'Andrew'},
            'body': 'God created men and women.'
        },
        {
            'author': {'username': 'Lucifer'},
            'body': 'But everything else is made in China.'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
