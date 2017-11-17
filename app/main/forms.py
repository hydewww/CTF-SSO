from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from .. import photos


class PhotoForm(FlaskForm):
    photo = FileField('Upload', validators=[
                                FileAllowed(photos, 'Only images'), 
                                FileRequired('Nothing chosen')
                                ])
    submit = SubmitField('Upload')
