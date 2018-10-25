# -*- coding:utf-8 -*-


import datetime
from faker import Factory
from app.baseapp import db
from app.models import Table
from app.models import User
from app.models import Province
from app.models import District

"""
https://lo.wikipedia.org/wiki/%E0%BA%9B%E0%BA%B0%E0%BB%80%E0%BA%97%E0%BA%94%E0%BA%A5%E0%BA%B2%E0%BA%A7
ຈໍານວນ	ຊື່ແຂວງ	ເນື້ອທີ່
ກມ²	ຈຳນວນ
ປະຊາກອນ	ຍິງ	ຊາຍ	ຄວາມໜາແໜ້ນ
ຄົນ/ກມ²
1	ອັດຕະປື	10.320	121.134	61.740	59.394	12
2	ບໍ່ແກ້ວ	6.196	157.422	79.116	78.306	25
3	ບໍລິຄຳໄຊ	14.863	248.378	122.738	125.641	17
4	ຈຳປາສັກ	15.415	634.756	319.886	314.870	41
5	ຫົວພັນ	16.500	302.809	150.095	152.714	18
6	ຄໍາມ່ວນ	16.315	360.304	183.070	177.234	22
7	ຫຼວງນ້ຳທາ	9.325	156.667	79.109	77.558	17
8	ຫຼວງພະບາງ	16.875	431.439	215.440	215.999	26
9	ອຸດົມໄຊ	15.370	285.874	143.161	142.713	19
10	ຜົ້ງສາລີ	16.270	172.286	85.830	86.456	11
11	ໄຊຍະບູລີ	16.839	360.195	178.301	181.893	22
12	ສາລະວັນ	10.691	349.478	177.856	171.622	33
13	ສະຫວັນນະເຂດ	21.774	874.660	442.866	431.794	40
14	ເຊກອງ	7.665	92.624	46.749	45.830	12
15	ນະຄອນຫຼວງວຽງຈັນ	3.920	740.010	370.293	369.717	189
16	ວຽງຈັນ	22.554	454.660	223.392	231.269	20
17	ຊຽງຂວາງ	16.358	257.683	127.652	130.031	16
"""

provinces = [
{ 'id': 1, 'name': 'ອັດຕະປື' },
{ 'id': 2, 'name': 'ບໍ່ແກ້ວ' },
{ 'id': 3, 'name': 'ບໍລິຄຳໄຊ' },
{ 'id': 4, 'name': 'ຈຳປາສັກ' } ,
{ 'id': 5, 'name': 'ຫົວພັນ' }, 
{ 'id': 6, 'name': 'ຄໍາມ່ວນ' },
{ 'id': 7, 'name': 'ຫຼວງນ້ຳທາ' },
{ 'id': 8, 'name': 'ຫຼວງພະບາງ' },
{ 'id': 9, 'name': 'ອຸດົມໄຊ' },
{ 'id': 10, 'name': 'ຜົ້ງສາລີ' },
{ 'id': 11, 'name': 'ໄຊຍະບູລີ' },
{ 'id': 12, 'name': 'ສາລະວັນ' },
{ 'id': 13, 'name': 'ສະຫວັນນະເຂດ' },
{ 'id': 14, 'name': 'ເຊກອງ' },
{ 'id': 15, 'name': 'ນະຄອນຫຼວງວຽງຈັນ' },
{ 'id': 16, 'name': 'ວຽງຈັນ' },
{ 'id': 17, 'name': 'ຊຽງຂວາງ' }
]

districts = [
    { 'id': 1, 'province_id': 15, 'name': 'ເມືອງຈັນທະບູລີ' }, # (1-01)
    { 'id': 2, 'province_id': 15, 'name': 'ເມືອງສີໂຄດຕະບອງ' }, # (1-02)
    { 'id': 3, 'province_id': 15, 'name': 'ເມືອງໄຊເສດຖາ' }, # (1-03)
    { 'id': 4, 'province_id': 15, 'name': 'ເມືອງສີສັດຕະນາກ' }, # (1-04)
    { 'id': 5, 'province_id': 15, 'name': 'ເມືອງນາຊາຍທອງ' }, # (1-05)
    { 'id': 6, 'province_id': 15, 'name': 'ເມືອງໄຊທານີ' }, # (1-06)
    { 'id': 7, 'province_id': 15, 'name': 'ເມືອງຫາດຊາຍຟອງ' }, # (1-07)
    { 'id': 8, 'province_id': 15, 'name': 'ເມືອງສັງທອງ' }, # (1-08)
    { 'id': 9, 'province_id': 15, 'name': 'ເມືອງປາກງື່ມ' } # (1-09)
]

tables = [
    { 'id': 1, 'name': 'real_estates' },
    { 'id': 2, 'name': 'cars' },
    { 'id': 3, 'name': 'products' },
]


fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
db.session.commit()

users = [
        {
            'first_name' : 'admin',
            'family_name' : 'admin',
            'username' : 'admin',
            'password' : 'admin',
            'email' : 'admin@gmail.com',
            'phone' : '000-1111-2222',
            'authority' : 0,
        },
        {
            'first_name' : 'lakadee',
            'family_name' : 'lakadee',
            'username' : 'lakadee',
            'password' : 'lakadee',
            'email' : 'lakadee@gmail.com',
            'phone' : '000-1111-3333',
            'authority' : 1,
        },
]

for o in users:
    user = User(authority=o['authority'], first_name=o['first_name'], family_name=o['family_name'], username=o['username'], password=o['password'], email=o['email'], phone=o['phone'])
    user.set_password(o['password'])
    db.session.add(user)
    db.session.commit()


for obj in tables:
    print(obj)
    table = Table(id=obj['id'], name=obj['name'])
    db.session.add(table)
    

for obj in provinces:
    print(obj)
    province = Province(id=obj['id'], name=obj['name'], created_at=datetime.datetime.today(), updated_at=datetime.datetime.today())
    db.session.add(province)

db.session.commit()

for obj in districts:
    print(obj)
    district = District(id=obj['id'], province_id=obj['province_id'], name=obj['name'], created_at=datetime.datetime.today(), updated_at=datetime.datetime.today())
    db.session.add(district)

db.session.commit()

"""
for num in range(100):
    fullname = fake.name().split()
    first_name = fullname[0]
    family_name = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    user = User(first_name=first_name, family_name=family_name, email=email, phone=phone)
    db.session.add(user)

db.session.commit()
"""
