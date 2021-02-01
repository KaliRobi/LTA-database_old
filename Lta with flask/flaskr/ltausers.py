from flask import Flask, Blueprint, render_template, g, request, url_for, session
import functools
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.lta_database import get_users_db


bp = Blueprint('users', __name__, url_prefix='/users' )


@bp.route('/login', methods=('GET', 'POST'))
def login_to_app():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_users_db()
        error = None
        user = get_users_db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = 'Username or password is incorrect'
        elif not check_password_hash(user['password'], password):
            error = 'Username or password is incorrect'
        
        if error is None:
            session.clear()
            session['user_id'] = user['Uiid']
            return 'you are in'




    return render_template('forusers.html')