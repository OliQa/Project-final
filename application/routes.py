

from flask import render_template, render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Gear, Users
from application.forms import RegisterForm, LoginForm, SetupForm, AccountUpdateForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
@app.route('/home')
def home():
	gearData = Gear.query.all()


	return render_template('home.html', title='Home' , gear=gearData)





@app.route('/about')
def about():
	return render_template('about.html', title='About')



@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data),
	    first_name=form.first_name.data,
	    last_name=form.last_name.data


        )












        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/setup', methods=['GET', 'POST'])
@login_required
def setup():
	form = SetupForm()
	if form.validate_on_submit():
		gear = Gear(
				build_id=current_user.id,
                                buildname=form.comment.data,
                                comment=form.comment.data,
                                weapon=form.weapon.data,
                                ammotype=form.ammotype.data,
                                bodyarmour=form.bodyarmour.data,
                                helmet=form.helmet.data
	)
		db.session.add(gear)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template("newclass.html", form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = AccountUpdateForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data


		db.session.commit()
		return redirect(url_for('home'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

