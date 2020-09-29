from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email, Required
from ..models import User
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed


class PostForm(FlaskForm):
    topic = StringField('Topic', validators=[InputRequired(message="Topic required")])
    category = SelectField('Category', choices=[('product', 'product'), ('interview', 'interview'), ('promotion', 'promotion')], validators=[InputRequired(message="Category required")])
    description = StringField('Description', validators=[InputRequired(message="Description required")])
    submit= SubmitField('Post')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('username', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    profile_pic_path = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Type Comment.',validators = [Required()])
    submit = SubmitField('Submit')