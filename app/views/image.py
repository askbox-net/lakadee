# -*- coding:utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.utils import secure_filename
from .. models import Image
from .. forms import ImageForm
from .. baseapp import app
from .. baseapp import db

from flask import Blueprint

image = Blueprint('image', __name__)


@app.route('/image/add/<id>',methods=['GET', 'POST'])
@login_required
def image_add(id):
    user_id = current_user.id
    print('user_id:', current_user.id)
    form = ImageForm(user_id=current_user.id, real_estate_id=id)
    print(form)

    if form.validate_on_submit():
        #filename = secure_filename(form.binary.file.filename)
        #file = request.files['file']
        print('file:', form.binary.data.filename)
        print('file:', vars(form.binary.data))
        print('mime:', form.binary.data.headers['Content-Type'])
        mime = form.binary.data.headers['Content-Type']

        form.binary.data.save('/tmp/xyz.jpg')
        image = Image(user_id=user_id, mime=mime)
        #print('filename:', filename)
        #form.populate_obj(image)
        db.session.add(image)

        #print(image.area, image.district_id)
        print(vars(image))
        try:
            db.session.commit()
            # User info
            flash('real_state created correctly', 'success')
            return redirect(url_for('real_estates'))
        except:
            db.session.rollback()
            flash('Error generating Real State.', 'danger')
        pass

    return render_template('web/image_new.html', form=form)

"""
@app.route('/images',methods=['GET','POST'])
@login_required
def images():
    '''
    Show alls real estate
    '''
    images = RealEstate.query.order_by(RealEstate.id).all()
    return render_template('web/images.html', images=images)

@app.route('/image/edit/<id>',methods=['GET','POST'])
@login_required
def image_edit(id):
    '''
    Edit user

    :param id: Id from user
    '''
    user_id = current_user.id
    image = RealEstate.query.filter_by(id=id, user_id=user_id).first()
    form = RealEstateForm(obj=image)
    if form.validate_on_submit():
        try:
            # Update user
            form.populate_obj(image)
            db.session.add(image)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update real estate.', 'danger')
    return render_template('web/image_edit.html', form=form)


@app.route('/image/add',methods=['GET','POST'])
@login_required
def image_add():
    user_id = current_user.id
    print('user_id:', current_user.id)
    form = RealEstateForm(user_id=current_user.id)
    print(form)

    if form.validate_on_submit():
        image = RealEstate()
        form.populate_obj(image)
        db.session.add(image)

        print(image.area, image.district_id)
        print(vars(image))
        try:
            db.session.commit()
            # User info
            flash('real_state created correctly', 'success')
            return redirect(url_for('image_add'))
        except:
            db.session.rollback()
            flash('Error generating Real State.', 'danger')
        pass

    return render_template('web/image_new.html', form=form)


@app.route("/image/delete", methods=('POST',))
@login_required
def image_delete():
    '''
    Delete real estate
    '''
    user_id = current_user.id
    try:
        image = RealEstate.query.filter_by(id=request.form['id'], user_id=user_id).first()
        db.session.delete(image)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  user.', 'danger')

    return redirect(url_for('images'))
"""
