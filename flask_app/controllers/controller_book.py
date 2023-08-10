from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_profile import Profile
from flask_app.models.model_user import User

@app.route("/user/bookshelf")
def users_bookshelf():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('my_library.html')