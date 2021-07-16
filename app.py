from flask import request, render_template, jsonify, url_for, redirect
from flask.helpers import url_for
from flask_login import logout_user

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .models import User

from . import create_app

app = create_app()


engine = create_engine('sqlite:///users.db')

DBSession = sessionmaker(engine)
session = DBSession()


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username is None or password is None:
            return jsonify({'message': 'missing argument'})
        user = session.query(User).filter_by(username=username).first()
        if not user: # create user's credentials
            user = session.query(User).filter_by(username=username).first()
            user = User(username =  username)
            user.hash_password(password)
            session.add(user)
            session.commit()
            return render_template('index.html', message = '{} created'.format(username))
        if not user.verify_password(password):
            return jsonify({'message': 'password mismatched'})
        return redirect(url_for('members'))
    return render_template('index.html', message = '')

@app.route("/members")
def members():
    return render_template('members.html')

@app.route("/logout", methods = ['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	