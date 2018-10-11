# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from .. forms import ProductForm
from .. baseapp import app
from .. baseapp import db

from flask import Blueprint

product = Blueprint('product', __name__)


@app.route('/product',methods=['GET','POST'])
def products():
    return render_template('web/product.html')


@app.route('/product/add',methods=['GET','POST'])
def product_add():
    form = ProductForm()
    return render_template('web/product_new.html', form=form)

