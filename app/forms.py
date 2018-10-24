# -*- coding:utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField, SelectField, SubmitField
from wtforms import IntegerField, FloatField
#from wtforms import FileField #, FileRequired, FileAllowed,
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, Length

from . baseapp import province_master, district_master


class UserForm(FlaskForm):
    first_name = StringField('ຊື່', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    family_name = StringField('ນາມສະກຸນ', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    username = StringField('Username', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    password = StringField('ລະຫັດຜ່ານ', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    email = StringField('ອີເມວ', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    phone = StringField('ເບີໂທລະສັບ', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])


class LoginForm(FlaskForm):
    username = StringField('Username / ອີເມວ / ເບີໂທລະສັບ', validators=[Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    password = StringField('ລະຫັດຜ່ານ', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    remember_me = BooleanField('Remember me')


class BaseForm(FlaskForm):
    #form_name = HiddenField('Form Name')
    id = HiddenField()
    user_id = HiddenField()
    #user_id = HiddenField(coerce=int)
    #user_id = IntegerField(widget=HiddenField())
    #user_id = IntegerField()
    email = StringField('ອີເມວ', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    phone = StringField('ເບີໂທລະສັບ', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])


class ProductForm(BaseForm):
    brand_id = HiddenField()
    categories = SelectField('Categories', validators=[DataRequired()], choices = [('cpp', 'C++'), ('py', 'Python')])#, id='select_state')
    #BooleanField
    name = StringField('ຊື່', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    #submit = SubmitField('Select County!')
    price = IntegerField('price', validators=[DataRequired(), Length(min=-1, max=32, message='You cannot have more than 32 characters')])


class CarForm(BaseForm):
    brand_id = HiddenField()


class ImageForm(BaseForm):
    binary = FileField('ຮູບພາບ', validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])
    real_estate_id = IntegerField()


class RealEstateForm(BaseForm):
    img_checksums = HiddenField()
    img_ids = HiddenField()
    img1 = HiddenField()
    img2 = HiddenField()
    img3 = HiddenField()
    img4 = HiddenField()
    img5 = HiddenField()
    img6 = HiddenField()
    table_id = HiddenField(default=1) 
    province_id = SelectField('ແຂວງ', coerce=int, validators=[DataRequired()], choices=province_master, default=15) #province_master[15])#, id='select_state')
    district_id = SelectField('ເມືອງ', coerce=int, validators=[DataRequired()], choices=district_master, default=1) #province_master[15])#, id='select_state')

    name = StringField('ຫົວຂໍ້', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    description = StringField('ລາຍລະອຽດ', validators=[DataRequired(), Length(min=-1, max=160, message='You cannot have more than 160 characters')])

    area = FloatField('ເນື້ອທີ່', validators=[DataRequired()])
    price = IntegerField('ລາຄາ', validators=[DataRequired()])
    #geo_x = FloatField('geo_x')#, validators=[DataRequired()])
    #geo_y = FloatField('geo_y')#, validators=[DataRequired()])

