# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from .. models import User
from .. forms import UserForm, LoginForm
from .. baseapp import app
from .. baseapp import db
from .. baseapp import login_manager

from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy import or_
from flask import Blueprint

car = Blueprint('car', __name__)

