#main views or url endpoints for front end aspect of our website
from flask import Blueprint, render_template
# this has a bunch of routes inside this file
views = Blueprint('views', __name__)

@views.route('/') # go slash main page will run -> this line is called the decorator
def home():
    return render_template("home.html")
