# -*- coding:utf-8 -*-


from faker import Factory
from app.baseapp import db
from app.models import User

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
for num in range(100):
    fullname = fake.name().split()
    first_name = fullname[0]
    family_name = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    mi_contacto = User(first_name=first_name, family_name=family_name, email=email, phone=phone)
    db.session.add(mi_contacto)

db.session.commit()
