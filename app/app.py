# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from . models import User
#from . import config
from . forms import UserForm
from . baseapp import app
from . baseapp import db



@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('users'))


@app.route("/users")
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
            db.session.add(my_user)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update user.', 'danger')
    return render_template(
        'web/edit_user.html',
        form=form)


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
