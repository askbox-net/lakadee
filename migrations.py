# -*- coding:utf-8 -*-


import datetime
from faker import Factory
from app.baseapp import db
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
'ອັດຕະປື',
'ບໍ່ແກ້ວ',
'ບໍລິຄຳໄຊ',
'ຈຳປາສັກ',
'ຫົວພັນ',
'ຄໍາມ່ວນ',
'ຫຼວງນ້ຳທາ',
'ຫຼວງພະບາງ',
'ອຸດົມໄຊ',
'ຜົ້ງສາລີ',
'ໄຊຍະບູລີ',
'ສາລະວັນ',
'ສະຫວັນນະເຂດ',
'ເຊກອງ',
'ນະຄອນຫຼວງວຽງຈັນ',
'ວຽງຈັນ',
'ຊຽງຂວາງ'
]

p15 = [
'ເມືອງຈັນທະບູລີ', # (1-01)
'ເມືອງສີໂຄດຕະບອງ', # (1-02)
'ເມືອງໄຊເສດຖາ', # (1-03)
'ເມືອງສີສັດຕະນາກ', # (1-04)
'ເມືອງນາຊາຍທອງ', # (1-05)
'ເມືອງໄຊທານີ', # (1-06)
'ເມືອງຫາດຊາຍຟອງ', # (1-07)
'ເມືອງສັງທອງ', # (1-08)
'ເມືອງປາກງື່ມ' # (1-09)
]

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
#db.drop_all()
db.create_all()
# Make 100 fake contacts
db.session.commit()


for province in provinces:
    print(province)
    province = Province(name=province, created_at=datetime.datetime.today(), updated_at=datetime.datetime.today())
    db.session.add(province)

db.session.commit()

for p in p15:
    print(p)
    district = District(province_id=15, name=p, created_at=datetime.datetime.today(), updated_at=datetime.datetime.today())
    db.session.add(district)

db.session.commit()

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
