from flask import Flask, render_template, url_for, request, session, redirect
from config import Development_Config as conf
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
    # if user is logged in setting up vars to be used in rendering the index template
    if session['log_in'] == True:
        username = User.get_username(session["uuid"])
        is_admin = User.is_admin(session["uuid"])
        email = User.get_email_by_id(session["uuid"])
        return view.render_template(view='home.html',username=username,admin=is_admin,email=email)
    else:
        return view.render_template(view='home.html')
@app.route('/auth',methods=['GET'])
def auth():
    return view.render_template(view='auth.html') 


@app.route('/reports/<string:')
@app.route('/reports',methodes=['GET'])
def reports(user_id=None):
    if session['log_in'] == True:
        return view.render_template(view='reports.html')
    else:
        redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    email= request.form['email']
    password = request.form['password']
    #TODO by Houssem 1- sanatize data passed from user
    print(User.valid_login(email,password))
    if User.valid_login(email,password):
        # Hacky code here <.<
        uuid = User.get_id_by_email(email)
        User.login(uuid)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('auth'))

@app.route('/logout',methods=['POST','GET'])
def logout():
	User.logout()
	return redirect(url_for('index'))

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['name']
        #TODO by houssem 1- sanatize data passed from user
        user = User.register(username,email,password)
        if user:
            return redirect(url_for('index'))
        return 'Account already exists!'
    return view.render_template(view='register.html')

@app.errorhandler(404)
def not_found(error):
    return view.render_template(view='error.html'), 404
if __name__ == '__main__':
    app.secret_key = conf.SECRET_KEY
app.run(debug=conf.DEBUG)