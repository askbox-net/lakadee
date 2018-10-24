# -*- coding:utf-8 -*-


from flask_sqlalchemy import SQLAlchemy
from .. baseapp import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json


class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


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
    authority = db.Column(db.Integer, nullable=False, default=1)
    first_name = db.Column(db.String(80), nullable=False)
    family_name = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(80), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    password_hash = db.Column(db.String(80))
    email = db.Column(db.String(200), nullable=True, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
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



class Item(object):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)

    price = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(160), nullable=True)

    category_ids = db.Column(db.String(80), nullable=True)
    #_img_ids = db.Column('img_ids', db.String(80), nullable=True)
    img_ids = db.Column(db.String(80), nullable=True)

    email = db.Column(db.String(200), nullable=True, unique=False)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    delete_flag = db.Column(db.Integer, default=0)
    complete_flag = db.Column(db.Integer, default=0)

    img1 = db.Column(db.Text, nullable=True, unique=False)
    img2 = db.Column(db.Text, nullable=True, unique=False)
    img3 = db.Column(db.Text, nullable=True, unique=False)
    img4 = db.Column(db.Text, nullable=True, unique=False)
    img5 = db.Column(db.Text, nullable=True, unique=False)
    img6 = db.Column(db.Text, nullable=True, unique=False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    """
    @property
    def img_ids(self):
        if self._img_ids and len(self._img_ids) == 0:
            return '[]'
        return self._img_ids
        #return json.loads(self._img_ids)

    @img_ids.setter
    def img_ids(self, ids):
        if ids and len(ids) > 0:
            self._img_ids = json.dumps(ids)
        else:
            self._img_ids = '[]'
    """

class Product(Item, db.Model):
    __tablename__ = 'products'

    brand_id = db.Column(db.Integer, index=True)
    distance = db.Column(db.Integer)


class Car(Item, db.Model):
    __tablename__ = 'cars'

    brand_id = db.Column(db.Integer, index=True)
    distance = db.Column(db.Integer, index=True)


class RealEstate(Item, db.Model):
    __tablename__ = 'real_estates'

    province_id = db.Column(db.Integer, index=True)
    district_id = db.Column(db.Integer, index=True)
    geo_x = db.Column(db.Float)
    geo_y = db.Column(db.Float)
    area = db.Column(db.Float)



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    table_id = db.Column(db.Integer, nullable=True)
    item_id = db.Column(db.Integer, nullable=True)
    checksum = db.Column(db.String(32), nullable=True)
    mime = db.Column(db.String(24), nullable=True)
    binary = db.Column(db.Binary())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

