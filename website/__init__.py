# make website folder a python package, we can import website folder and whatever is in this init.py file, it can run automatically when we iimport 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# from werkzeug.datastructures import D

db = SQLAlchemy() # object to manipulate the database
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # __name represents the name of the file
    app.config['SECRET_KEY'] = 'confidence123' # secret key for encryption of cookies and session data related to our website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # store this database inside the website folder {python code evaluates to string}
    db.init_app(app) # intialize our database using our flask app 

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix = '/') # no prefixes

    from .models import User, Note # define our classes for us, rename what we have imported without a . in the beginning

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')