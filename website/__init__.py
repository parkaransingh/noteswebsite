# make website folder a python package, we can import website folder and whatever is in this init.py file, it can run automatically when we iimport 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # object to manipulate the database
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # __name represents the name of the file
    app.config['SECRET_KEY'] = 'confidence123' # secret key for encryption of cookies and session data related to our website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # store this database inside the website folder

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix = '/') # no prefixes
    return app
    