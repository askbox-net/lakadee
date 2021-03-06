# -*- coding:utf-8 -*-


import json
from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from .. models import RealEstate
from .. forms import RealEstateForm
from .. baseapp import app
from .. baseapp import db
from .. models import Image
#from sqlalchemy import or_
from sqlalchemy import desc

from flask import Blueprint

real_estate = Blueprint('real_estate', __name__)


@app.route('/real_estates',methods=['GET','POST'])
@login_required
def real_estates():
    '''
    Show alls real estate
    '''
    user_id = current_user.id
    real_estates = RealEstate.query.filter(RealEstate.user_id==user_id).order_by(desc(RealEstate.id)).all()
    return render_template('web/real_estates.html', real_estates=real_estates)


@app.route('/real_estate/new',methods=['GET','POST'])
@login_required
def real_estate_new():
    user_id = current_user.id
    user_email = current_user.email
    user_phone = current_user.phone
    print('user_id:', current_user.id, user_email, user_phone)
    form = RealEstateForm(id=None, user_id=user_id, email=user_email, phone=user_phone)
    print(vars(form))

    if form.validate_on_submit():
        real_estate = RealEstate()
        form.populate_obj(real_estate)
        real_estate.id = None
        print(vars(real_estate))
        db.session.add(real_estate)

        #print(real_estate.area, real_estate.district_id)
        #print(vars(real_estate))
        try:
            db.session.commit()
            # User info
            flash('real_state created correctly', 'success')
            #return redirect(url_for('real_estate_new'))
            return redirect(url_for('real_estates'))
        except:
            db.session.rollback()
            flash('Error generating Real State.', 'danger')

    #real_estate = RealEstate.query.filter_by(user_id=user_id).first()
    #form = RealEstateForm(obj=real_estate)
    #return render_template('web/real_estate_new.html', form=form)
    return render_template('web/real_estate_edit.html', form=form)

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
            """
            print('form:', vars(form))
            print('form img_checksums:', vars(form.img_checksums))
            img_checksums = json.loads(form.img_checksums.data)
            print('img_checksums: ', img_checksums)
            imgs = Image.query.filter(Image.checksum.in_(img_checksums)).all()
            #imgs = Image.query.filter().all()
            ids = []
            for o in imgs:
                ids.append(o.id)
            form.populate_obj(real_estate)
            print('ids ---> ')
            print(json.dumps(ids))
            real_estate.img_ids = json.dumps(ids)
            """
            form.populate_obj(real_estate)
            db.session.add(real_estate)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
            return redirect(url_for('real_estates'))
        except:
            db.session.rollback()
            flash('Error update real estate.', 'danger')
    return render_template('web/real_estate_edit.html', form=form)


@app.route("/real_estate/search", methods=('POST', 'GET'))
@login_required
def real_estate_search():
    '''
    Delete real estate
    '''
    user_id = current_user.id
    try:
        pass
    except:
        pass

    return redirect(url_for('real_estates'))


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

