from flask import Flask, render_template, url_for, request, session, redirect
from config import BaseConfig as conf
from utils.Database import Database as base
from models.Usermodel import User

import os

app = Flask(__name__)


@app.before_first_request
def initial():
	base.initialize()

@app.route('/')
def index():
    if 'email' in session:
        return 'You are logged in as ' + session['email']

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email= request.form['email']
    password = request.form['password']
    if User.valid_login(email,password):
        User.login(email)
        return redirect(url_for('index'))

    return 'Invalid username/password combination'
@app.route('/logout',methods=['POST','GET'])
def logout():
	User.logout()
	return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
    	email = request.form['email']
    	password = request.form['password']
    	user = User.register(email,password)
    	if user:
    		return redirect(url_for('index'))
    	return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = conf.SECRET_KEY
app.run(debug=conf.DEBUG)