# -*- coding:utf-8 -*-


import tempfile
import filetype
import re
import json
from flask import Flask, redirect, url_for, render_template, request, flash, Response
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.utils import secure_filename
from .. models import Image
from .. forms import ImageForm
from .. baseapp import app
from .. baseapp import db
from .. models import Image

from flask import Blueprint

image = Blueprint('image', __name__)


@app.route('/image/<user_id>/<id>',methods=['GET'])
def image_id(user_id, id):
    img = Image.query.filter(Image.user_id==user_id, Image.id==id).first()

    if img:
        print(user_id, id)
        print('mime:', img.mime)

        return Response(response=img.binary, content_type=img.mime)

    return ''


@app.route('/image/new',methods=['POST'])
@login_required
def image_new():
    user_id = current_user.id

    if request.method == 'POST':
        binary = request.form['binary']
        user_id = request.form['user_id']
        table_id = request.form['table_id']
        base_id = request.form['base_id']
        binary = request.form['binary']
        checksum = request.form['checksum']
        mime = request.form['mime']

        print('base_id = ', base_id)
        #print('form = ', request.form)
        import base64
        import mimetypes

        try:
            #imgdata = re.sub('^data:image/.+;base64,', '', binary)
            imgdata = base64.b64decode(binary)
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                tf.write(imgdata)
                temp_filename = tf.name

            #mime = filetype.guess(temp_filename).mime
            print('mime : ', mime)
            with open(temp_filename, 'rb') as fp:
                binary = fp.read()

            #image = Image(user_id=user_id, table_id=table_id, base_id=base_id, mime=mime, binary=binary)
            image = Image(user_id=user_id, table_id=table_id, checksum=checksum, mime=mime, binary=binary)
            #print('filename:', filename)
            #form.populate_obj(image)
            db.session.add(image)
            db.session.commit()
            # User info
            #flash('real_state created correctly', 'success')
            #return redirect(url_for('real_estates'))
            from sqlalchemy import desc
            img = Image.query.filter(Image.user_id==user_id, Image.table_id==table_id).order_by(desc(Image.id)).first()
            data = {
                    'id': img.id
            }
            return json.dumps(data)

        except Exception as e:
            print('error:', e)

            db.session.rollback()
            flash('Error generating Real State.', 'danger')

    return ''


@app.route('/image/new/<id>',methods=['GET', 'POST'])
@login_required
def image_new_id(id):
    user_id = current_user.id
    form = ImageForm(user_id=current_user.id, real_estate_id=id)
    #print(form)

    if form.validate_on_submit():
        #filename = secure_filename(form.binary.file.filename)
        #file = request.files['file']
        #print('file:', form.binary.data.filename)
        #print('file:', vars(form.binary.data))
        #print('mime:', form.binary.data.headers['Content-Type'])
        mime = form.binary.data.headers['Content-Type']

        with tempfile.NamedTemporaryFile(delete=False) as tf:
            form.binary.data.save(tf)
            temp_filename = tf.name

        with open(temp_filename, 'rb') as fp:
            binary = fp.read()

        image = Image(user_id=user_id, mime=mime, binary=binary)
        #print('filename:', filename)
        #form.populate_obj(image)
        db.session.add(image)

        #print(image.area, image.district_id)
        #print(vars(image))
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


"""
#@app.route('/image/new',methods=['GET','POST'])
#@login_required
#def image_new():
#    user_id = current_user.id
#    print('user_id:', current_user.id)
#    form = RealEstateForm(user_id=current_user.id)
#    print(form)
#
#    if form.validate_on_submit():
#        image = RealEstate()
#        form.populate_obj(image)
#        db.session.add(image)
#
#        print(image.area, image.district_id)
#        print(vars(image))
#        try:
#            db.session.commit()
#            # User info
#            flash('real_state created correctly', 'success')
#            return redirect(url_for('image_new'))
#        except:
#            db.session.rollback()
#            flash('Error generating Real State.', 'danger')
#        pass
#
#    return render_template('web/image_new.html', form=form)
"""


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
