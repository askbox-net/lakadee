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

user = Blueprint('user', __name__)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('users'))



@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    #else haven't login, ask for login
    form = LoginForm()
    if form.validate_on_submit():
        #find the user
        username = form.username.data
        user = User.query.filter(or_(User.username==username, User.email==username, User.phone==username)).first()
        #user = User.query.filter((User.username==username) | (User.email==username) | (User.phone==username)).first()
        print(user)
        print('password:', form.password.data)
        if user is None or not user.check_password(form.password.data):
            #no such password or wrong password
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        #else ,login success
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('web/login.html',title='Sign in',form=form)


@app.route("/logout")
#@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



@app.route("/users")
#@login_required
def users():
    '''
    Show alls users
    '''
    users = User.query.order_by(User.first_name).all()
    return render_template('./web/users.html', users=users)


@app.route("/user/new", methods=('GET', 'POST'))
def user_new():
    '''
    Create new user
    '''
    form = UserForm()
    if form.validate_on_submit():
        my_user = User()
        my_user.set_password(form.password.data)
        form.populate_obj(my_user)
        db.session.add(my_user)
        try:
            db.session.commit()
            # User info
            flash('User created correctly', 'success')
            return redirect(url_for('users'))
        except:
            db.session.rollback()
            flash('Error generating user.', 'danger')

    return render_template('web/user_new.html', form=form)


@app.route("/user/edit/<id>", methods=('GET', 'POST'))
def user_edit(id):
    '''
    Edit user

    :param id: Id from user
    '''
    my_user = User.query.filter_by(id=id).first()
    form = UserForm(obj=my_user)
    if form.validate_on_submit():
        try:
            # Update user
            form.populate_obj(my_user)
            my_user.set_password(form.password.data)
            db.session.add(my_user)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update user.', 'danger')
    return render_template('web/user_edit.html', form=form)


@app.route("/search")
def search():
    '''
    Search
    '''
    name_search = request.args.get('first_name')
    all_users = User.query.filter(
        User.first_name.contains(name_search)
        ).order_by(User.first_name).all()
    return render_template('web/users.html', users=all_users)


@app.route("/user/delete", methods=('POST',))
def user_delete():
    '''
    Delete user
    '''
    try:
        mi_user = User.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_user)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  user.', 'danger')

    return redirect(url_for('users'))

