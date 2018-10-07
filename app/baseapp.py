# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
"""


# Flask
app = Flask(__name__)
app.config.from_object('config')

print(app.config)

# SQL
db = SQLAlchemy(app)

