# -*- coding:utf-8 -*-


from flask_sqlalchemy import SQLAlchemy
from .. baseapp import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    family_name = db.Column(db.String(100), nullable=True)
    nickname = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return '<Users %r>' % self.first_name
