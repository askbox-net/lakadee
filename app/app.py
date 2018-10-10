# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from . models import User
from . forms import UserForm, LoginForm, ItemForm
from . baseapp import app
from . baseapp import db
from . baseapp import login_manager

from flask_login import login_required, current_user, login_user, logout_user
from urllib.parse import urlparse, urljoin
from sqlalchemy import or_

"""
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

"""

@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('users'))



@app.route('/item',methods=['GET','POST'])
def item():
    form = ItemForm()
    return render_template('web/item.html', form=form)
    #return "yxz" 

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
def load_user(user_id):
        return User()

"""
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
"""

"""
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
"""

"""
@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')
"""


@app.route("/users")
#@login_required
def users():
    '''
    Show alls users
    '''
    users = User.query.order_by(User.first_name).all()
    return render_template('./web/users.html', users=users)


@app.route("/new_user", methods=('GET', 'POST'))
def new_user():
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

    return render_template('web/new_user.html', form=form)


@app.route("/edit_user/<id>", methods=('GET', 'POST'))
def edit_user(id):
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
    return render_template('web/edit_user.html', form=form)


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


@app.route("/users/delete", methods=('POST',))
def users_delete():
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


"""
if __name__ == "__main__":
    app.run(host="0.0.0.0")
"""
