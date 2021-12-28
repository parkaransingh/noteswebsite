from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)
# get is retrieving information 
# post change to state of the system or database ex post request of signing in
# update, delete, put
@auth.route('/login', methods=['GET', 'POST']) # did we send a get or post request, GOING TO URL IS GET REQUEST, POST REQUEST IS THE SUBMISSION OF LOGIN BUTTON 
def login():
    # data = request.form # request variable inside a root will have information of the request sent to access this route, we can access the form data using .form
    # print(data) # will print a immutatable multi Dict
    return render_template("login.html", boolean = True)
@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # differentiate get and post request 
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # few python checks with message flashing
        if len(email) < 4:
            flash('Email must be greater than or equal to 4 characters.', category = 'error')
        elif len(firstName) < 2:
            flash('First name must be greater than or equal to 2 characters.', category = 'error')
        elif password1 != password2:
            flash('Passwords do not match', category = 'error')
        elif len(password1) < 7:
            flash('Passwords must be greater than or equal to 7 characters.', category = 'error')
        else:
            flash('Account created!', category = 'success')
    return render_template("sign_up.html")
