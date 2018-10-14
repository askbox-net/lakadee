# -*- coding:utf-8 -*-


from flask_sqlalchemy import SQLAlchemy
from .. baseapp import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Province(db.Model):
    __tablename__ = 'provinces'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class District(db.Model):
    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


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



class Base(object):
    #__tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)

    price = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(160), nullable=False)

    category_ids = db.Column(db.String(80), nullable=True)
    img_ids = db.Column(db.String(80), nullable=True)

    #email = db.Column(db.String(200), nullable=True, unique=False)
    #phone = db.Column(db.String(20), nullable=True, unique=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class Product(Base, db.Model):
    __tablename__ = 'products'

    brand_id = db.Column(db.Integer)
    distance = db.Column(db.Integer)


class Car(Base, db.Model):
    __tablename__ = 'cars'

    brand_id = db.Column(db.Integer)
    distance = db.Column(db.Integer)


class RealEstate(Base, db.Model):
    __tablename__ = 'real_estates'

    province_id = db.Column(db.Integer)
    district_id = db.Column(db.Integer)
    geo_x = db.Column(db.Float)
    geo_y = db.Column(db.Float)
    area = db.Column(db.Float)



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    mime = db.Column(db.String(24), nullable=False)
    binary = db.Column(db.Binary())

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

