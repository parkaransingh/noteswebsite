#main views or url endpoints for front end aspect of our website
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
# this has a bunch of routes inside this file
from .models import Note
from . import db
import json 
views = Blueprint('views', __name__)

@views.route('/', methods =['GET', 'POST']) # go slash main page will run -> this line is called the decorator
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('No text has been entered', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success')
            # change line 24 fix for post request reload
            return redirect(url_for('views.home'))
    return render_template("home.html", user=current_user)
@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id: # security check 
            db.session.delete(note)
            db.session.commit()
    return jsonify({})