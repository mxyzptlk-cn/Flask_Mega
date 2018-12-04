#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# The bottom import is a workaround to 'circular imports'.
from app import routes
