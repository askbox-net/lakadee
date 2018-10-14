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

# Master Data
province_master = []
district_master = []

def init_master():
    from app.models import Province
    from app.models import District
    provinces = Province.query.order_by(Province.id).all()
    districts = District.query.order_by(District.id).all()

    for province in provinces:
        #province_master.append((str(province.id), province.name))
        province_master.append((province.id, province.name))
    #province_master.insert(0, ('','year'))

    for district in districts:
        print(district.id, district.province_id, district.name)
        #district_master.append((str(district.id), district.name))
        district_master.append((district.id, district.name))
    #district_master.insert(0, ('','year'))


