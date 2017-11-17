from flask import render_template
from . import main
from .forms import PhotoForm
from .. import photos
from flask_login import current_user, login_required
from ..models import User
import os


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/photo', methods=['GET', 'POST'])
@login_required
def photo():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = "faces/" + current_user.name + "." + form.photo.data.filename.rsplit('.', 1)[1]
        try:
            file_path = photos.path(filename)
            os.remove(file_path)
        except:
            pass
        filename = photos.save(form.photo.data, name=filename)
        file_url = photos.url(filename)
        print(file_path, file_url)
    else:
        file_url = None
    
    if file_url == None:
        file_url = photos.url('faces/default.jpg')
    return render_template('main/photo.html', form=form, file_url=file_url, photos=photos)
