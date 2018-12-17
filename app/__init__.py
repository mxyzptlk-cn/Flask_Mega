#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-11-29

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# The bottom import is a workaround to 'circular imports'.
from app import routes, models
