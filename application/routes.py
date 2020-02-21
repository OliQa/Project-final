from flask import render_template, render_template, url_for, redirect
from application import app, db, bcrypt
from application.models import Gear
from application.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')
@app.route('/about')
def about():
	return render_template('about.html', title='About')



@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('register.html', title='Register')

