#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from flask import Flask

app = Flask(__name__)

# The bottom import is a workaround to 'circular imports'.
from app import routes
