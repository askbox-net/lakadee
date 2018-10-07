# -*- coding:utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    first_name = StringField('ຊື່', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    family_name = StringField('ນາມສະກຸນ', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    password = StringField('ລະຫັດຜ່ານ', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    email = StringField('ອີເມວ', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    phone = StringField('ເບີໂທລະສັບ', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])
