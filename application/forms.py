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
	buildname = StringField('Build name: ', validators=[DataRequired()])
	comment = StringField('Comment:')
	weapon = SelectField('Weapon select', choices=[('ADAR 2-5', 'ADAR 2-5'), ('AK-101', 'AK-101'), ('AK-74', 'AK-74'), ('HK 416A5', 'HK 416A5'), ('M4A1', 'M4A1')])
	ammotype = SelectField('Ammo select', choices=[('5.56x45mm', '5.56x45mm'), ('7.62x39mm', '7.62x39mm')])
	bodyarmour = SelectField('Bodyarmour select', choices=[('PACA Soft Armor', 'PACA Soft Armor'), ('MF-UNTAR Vest', 'MF-UNTAR Vest'), ('6B13 Assault armor', '6B13 Assault armor')])
	helmet = SelectField('Helmet select', choices=[('Soft Tank Crew', 'Soft Tank Crew'), ('PSH-97 "Djeta" helmet', 'PSH-97 "Djeta" helmet'), ('6B47 Ratnik-BSh Helmet', '6B47 Ratnik-BSh Helmet')])

	submit =SubmitField('Submit')
