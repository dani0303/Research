from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class UserForm(FlaskForm):
	picture = StringField('picture')
