# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, DateTime, Float, Binary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
 
SBase = declarative_base()

class Base(object):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)

    price = Column(Integer)
    name = Column(String(80), nullable=True)
    description = Column(String(160), nullable=True)

    category_ids = Column(String(80), nullable=True)
    #_img_ids = Column('img_ids', String(80), nullable=True)
    img_ids = Column(String(80), nullable=True)

    email = Column(String(200), nullable=True, unique=False)
    phone = Column(String(20), nullable=True, unique=False)

    delete_flag = Column(Integer, default=0)
    complete_flag = Column(Integer, default=0)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class RealEstate(Base, SBase): 
    __tablename__ = 'real_estates'

    province_id = Column(Integer, index=True)
    district_id = Column(Integer, index=True)
    geo_x = Column(Float)
    geo_y = Column(Float)
    area = Column(Float)



class Image(SBase):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    table_id = Column(Integer, nullable=True)
    base_id = Column(Integer, nullable=True)
    checksum = Column(String(32), nullable=True)
    mime = Column(String(24), nullable=True)
    binary = Column(Binary())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

dbname = "../app/lakadee.sqlite"
engine = create_engine('sqlite:///%s' % dbname, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    checksums = ['e1c60debb995243509daa2b4013a3269', '52dc2b341b7370377a397196e345a628']
    imgs = session.query(Image).filter(Image.checksum.in_(checksums)).all()
    for o in imgs:
        print(o.id, o.mime, o.checksum)

