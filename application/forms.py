from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import Users

class RegisterForm(FlaskForm):
	email = StringField('Email',
	validators = [
			DataRequired(),
			Email()
		]
	)
	password = PasswordField('Password',
	validators = [
			DataRequired(),
		]
	)
	confirm_password = PasswordField('Confirm Password',
	validators = [
			DataRequired(),
			EqualTo('password')
		]
	)
class LoginForm(FlaskForm):
	email = StringField('Email',
	validators = [
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
	validators = [
			DataRequired()
		]
	)

