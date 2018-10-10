# -*- coding:utf-8 -*-


from flask_sqlalchemy import SQLAlchemy
from .. baseapp import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    family_name = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(80), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    password_hash = db.Column(db.String(80))
    email = db.Column(db.String(200), nullable=True, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<Users %r>' % self.first_name



class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    brand_id = db.Column(db.Integer)

    price = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    img_ids = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    mime = db.Column(db.String(24), nullable=False)
    binary = db.Column(db.Binary())

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

