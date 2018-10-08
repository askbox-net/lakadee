# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login



# Flask
app = Flask(__name__)
app.config.from_object('config')

app.secret_key = 'lakadee secret' #'super secret string'


print(app.config)

# SQL
db = SQLAlchemy(app)

# Login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
#login_manager.login_view = 'web/login.html'
#login_manager.login_view = 'login'

