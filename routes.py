
from flask import request, jsonify, redirect, url_for, render_template
from flask_login import logout_user, login_required, current_user, login_user

from models import User
from config import session

def create_routes(app):
    @app.route("/", methods = ['GET', 'POST'])
    def index():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username is None or password is None or \
                len(username) == 0 or len(password) == 0:
                return render_template('index.html', message = 'missing argument'), 501
            user = session.query(User).filter_by(username=username).first()
            if user is None: # create user's credentials
                return render_template('index.html', message = 'user not exist'), 504
            if not user.verify_password(password): # verify user
                return render_template('index.html', message = 'password not mismatch'), 502
            login_user(user)
            return redirect(url_for('members'), code=201)
        return render_template('index.html', message = ''), 200
    
    @app.route("/signup", methods = ['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username is None or password is None or \
                len(username) == 0 or len(password) == 0:
                return render_template('signup.html', message = 'missing argument'), 501
            user = session.query(User).filter_by(username=username).first()
            print(user)
            if user is None:
                user = User(username=username, password=password)
                user.hash_password(password)
                session.add(user)
                session.commit()
                return redirect(url_for('index'), code=201)
            else:
                return render_template('signup.html', message = 'user exists'), 503
        return render_template('signup.html', message = ''), 200

    @app.route("/members")
    @login_required
    def members():
        return render_template('members.html', name=current_user.username), 200

    @app.route("/logout", methods = ['POST'])
    def logout():
        logout_user()
        return redirect(url_for('index'), code=201)
