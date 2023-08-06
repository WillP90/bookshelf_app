from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_user import User
from flask_app.models.model_profile import Profile

@app.route('/new/profile/<int:user_id>')
def new_page(user_id):
    return render_template('new_profile.html', user_id = user_id)

@app.post('/new/profile/process')
def process_profile():
    data ={
        "genre" : request.form['genre'],
        "location" : request.form['location'],
        "info" : request.form['info'],
        "user_id" : request.form['user_id']
    }
    profile = Profile.save_user_profile(data)
    return redirect('/profile')

@app.route('/edit/profile/<int:user_id>')
def edit_page(user_id):
    return render_template('edit_profile.html', user_id = user_id)