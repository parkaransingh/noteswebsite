# make website folder a python package, we can import website folder and whatever is in this init.py file, it can run automatically when we iimport 
from flask import Flask
def create_app():
    app = Flask(__name__) # __name represents the name of the file
    app.config['SECRET_KEY'] = 'confidence123' # secret key for encryption of cookies and session data related to our website
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix = '/') # no prefixes
    return app
    