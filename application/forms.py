from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import Users, Gear
from flask_login import current_user

class RegisterForm(FlaskForm):



	first_name = StringField('First Name',
	validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	last_name = StringField('Last Name',
	validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
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










	submit = SubmitField('Regsiter')







class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SetupForm(FlaskForm):


	buildname = StringField('Build name: ', validators=[DataRequired()])
	comment = StringField('Comment:')
	weapon = SelectField('Weapon select', choices=[('ADAR 2-5', 'ADAR 2-5'), ('AK-101', 'AK-101'), ('AK-74', 'AK-74')])
	ammotype = SelectField('Ammo select', choices=[('5.56x45mm', '5.56x45mm'), ('7.62x39mm', '7.62x39mm')])
	bodyarmour = SelectField('Bodyarmour select', choices=[('PACA Soft Armor', 'PACA Soft Armor')])
	helmet = SelectField('Helmet select', choices=[('Soft Tank Crew', 'Soft Tank Crew')])

	submit = SubmitField('Submit')



class AccountUpdateForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self,email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use')

