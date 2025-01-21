from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, ValidationError, Optional
from app.models import User

def email_in_use(form, field):
    email = field.data
    if email:
        user = User.query.filter(User.email == email).filter(User.id != form.current_user_id).first()
        if user:
            raise ValidationError('Email address is already in use.')

def username_in_use(form, field):
    username = field.data
    if username:
        user = User.query.filter(User.username == username).filter(User.id != form.current_user_id).first()
        if user:
            raise ValidationError('Username is already in use.')

class UpdateAccountForm(FlaskForm):
    current_user_id = None
    username = StringField('username', validators=[Optional(), username_in_use])
    email = StringField('email', validators=[Optional(), Email(), email_in_use])
    fname = StringField('fname', validators=[Optional()])
    lname = StringField('lname', validators=[Optional()])
    profile_picture = StringField('profile_picture', validators=[Optional()])
    banner_url = StringField('banner_url', validators=[Optional()])
