from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import Users, Gear


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
	weapon = SelectField('weapon select', choices=[('ADAR', 'ADAR 2-5'), ('AK1', 'AK-101'), ('AK2', 'AK-74'), ('HK1', 'HK 416A5'), ('M4', 'M4A1')])
	ammotype = SelectField('Ammo select', choices=[('5', '5.56x45mm'), ('7', '7.62x39mm')])
	bodyarmor = SelectField('Bodyarmor select', choices=[('paca', 'PACA Soft Armor'), ('mf', 'MF-UNTAR Vest'), ('assault', '6B13 Assault armor')])
	helmet = SelectField('Helmet select', choices=[('tank', 'Soft Tank Crew'), ('PSH', 'PSH-97 "Djeta" helmet'), ('6B47', '6B47 Ratnik-BSh Helmet')])

	submit =SubmitField('Submit')
