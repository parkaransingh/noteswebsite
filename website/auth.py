from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db # form the init.py file 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
# get is retrieving information 
# post change to state of the system or database ex post request of signing in
# update, delete, put
@auth.route('/login', methods=['GET', 'POST']) # did we send a get or post request, GOING TO URL IS GET REQUEST, POST REQUEST IS THE SUBMISSION OF LOGIN BUTTON 
def login():
    # data = request.form # request variable inside a root will have information of the request sent to access this route, we can access the form data using .form
    # print(data) # will print a immutatable multi Dict
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # QUERY the database look for certain entries
        user = User.query.filter_by(email = email).first() # return the first result, if we do we only have one beacuse it is a primary key 
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True) # remembers that we are loginned, as long as the session is still running, dont need to login everytime 
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User email does not exist, please try again or create account', category = 'error')


    return render_template("login.html", user = current_user)
@auth.route('/logout')
@login_required # decorator that makes sure you are logged in to access this
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # differentiate get and post request 
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email = email).first() # return the first result, if we do we only have one beacuse it is a primary key 
        # few python checks with message flashing
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than or equal to 4 characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First name must be greater than or equal to 2 characters.', category = 'error')
        elif password1 != password2:
            flash('Passwords do not match', category = 'error')
        elif len(password1) < 7:
            flash('Passwords must be greater than or equal to 7 characters.', category = 'error')
        else:
            new_user = User(email=email, first_name= first_name, password=generate_password_hash(password1, method='sha256')) # sha 256 hashing algorithm
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True) # remembers that we are loginned, as long as the session is still running, dont need to login everytime 
            flash('Account created!', category = 'success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user = current_user)
