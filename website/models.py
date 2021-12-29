# database models for our user and notes
from . import db # importing from the current package directory, the website folder the db object
from flask_login import UserMixin # module that helps login, in herite from UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now) # func current date and time
    # all notes must be associated with a User, set a through relationship which is carried through foreign key
    # foreign key is id of the user who created the note 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 1 - N relationship User class in sql is referenced through user lower case for foreign key

# we can add another Class for lets say reminders or video ------------ look at sql alchemy 
class User(db.Model, UserMixin): #inherit from sqlaclhemy object and UserMixin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True) # max length is 150
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # every time we create a note, create a list of all the notes in the this relationship, capital for the relationship for the name of the  class
