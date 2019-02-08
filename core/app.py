from flask import Flask, url_for, request, session, redirect
from config import BaseConfig as conf
from config import StaticVars as static_vars
from utils.Database import Database as base
from models.Usermodel import User
from view.viewer import view

import os

app = Flask(__name__)


@app.before_first_request
def initial():
	base.initialize()
@app.route('/')
def index():
    return view.render_template('home.html')
@app.route('/auth')
def auth():
    error=None
    if session['log_in']==True:
        return redirect(url_for('index'))
    else:
        error="Wrong credentials"
        return view.render_template('auth.html',error=error)

@app.route('/login', methods=['POST'])
def login():
    email= request.form['email']
    password = request.form['password']
    #TODO by Houssem 1- sanatize data passed from user
    if User.valid_login(email,password):
        # Hacky code here <.<
        uuid = User.get_id_by_email(email)
        User.login(uuid)
        return redirect(url_for('index'))

    return redirect(url_for('auth'))
@app.route('/logout',methods=['POST','GET'])
def logout():
	User.logout()
	return view.render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
    	email = request.form['email']
    	password = request.form['password']
#TODO by houssem 1- sanatize data passed from user
    	user = User.register(email,password)
    	if user:
    		return redirect(url_for('index'))
    	return 'Account already exists!'

    return view.render_template('register.html')

if __name__ == '__main__':
    app.secret_key = conf.SECRET_KEY
app.run(debug=conf.DEBUG)