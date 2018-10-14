# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from .. models import RealEstate
from .. forms import RealEstateForm
from .. baseapp import app
from .. baseapp import db

from flask import Blueprint

real_estate = Blueprint('real_estate', __name__)


@app.route('/real_estates',methods=['GET','POST'])
@login_required
def real_estates():
    '''
    Show alls real estate
    '''
    real_estates = RealEstate.query.order_by(RealEstate.id).all()
    return render_template('web/real_estates.html', real_estates=real_estates)

@app.route('/real_estate/edit/<id>',methods=['GET','POST'])
@login_required
def real_estate_edit(id):
    '''
    Edit user

    :param id: Id from user
    '''
    user_id = current_user.id
    real_estate = RealEstate.query.filter_by(id=id, user_id=user_id).first()
    form = RealEstateForm(obj=real_estate)
    if form.validate_on_submit():
        try:
            # Update user
            form.populate_obj(real_estate)
            db.session.add(real_estate)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update real estate.', 'danger')
    return render_template('web/real_estate_edit.html', form=form)


@app.route('/real_estate/add',methods=['GET','POST'])
@login_required
def real_estate_add():
    user_id = current_user.id
    print('user_id:', current_user.id)
    form = RealEstateForm(user_id=current_user.id)
    print(form)

    if form.validate_on_submit():
        real_estate = RealEstate()
        form.populate_obj(real_estate)
        db.session.add(real_estate)

        print(real_estate.area, real_estate.district_id)
        print(vars(real_estate))
        try:
            db.session.commit()
            # User info
            flash('real_state created correctly', 'success')
            return redirect(url_for('real_estate_add'))
        except:
            db.session.rollback()
            flash('Error generating Real State.', 'danger')
        pass

    return render_template('web/real_estate_new.html', form=form)


@app.route("/real_estate/delete", methods=('POST',))
@login_required
def real_estate_delete():
    '''
    Delete real estate
    '''
    user_id = current_user.id
    try:
        real_estate = RealEstate.query.filter_by(id=request.form['id'], user_id=user_id).first()
        db.session.delete(real_estate)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  user.', 'danger')

    return redirect(url_for('real_estates'))
