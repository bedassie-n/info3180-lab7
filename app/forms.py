from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField
from wtforms.validators import DataRequired, AnyOf

class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[DataRequired()])
    photo = FileField("Photo", validators=[DataRequired()], )

