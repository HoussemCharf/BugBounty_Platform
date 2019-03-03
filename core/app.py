from flask import Flask, render_template, url_for, request, session, redirect
from config import Development_Config as conf
from config import StaticVars as static_vars
from utils.Database import Database as base
from utils.sanatize import check_email, ready_to_get_banned,check_password,check_username
from models.Usermodel import User
from models.ReportModel import Report 
from view.viewer import view
import os



app = Flask(__name__)

@app.before_first_request
def initial():
	base.initialize()
@app.route('/')
def index():
    # if user is logged in setting up vars to be used in rendering the index template
    if session.get('log_in') != None: 
        if session['log_in'] == True:
            username = User.get_username(session["uuid"])
            is_admin = User.is_admin(session["uuid"])
            email = User.get_email_by_id(session["uuid"])
            return view.render_template(view='home.html',username=username,admin=is_admin,email=email)
    return view.render_template(view='home.html')
@app.route('/auth',methods=['GET'])
def auth():
    return view.render_template(view='auth.html') 
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
@app.route('/reports',methods=['GET'])
def reports():
    if session['log_in'] == True:
        _id = session['uuid']
        username = User.get_username(session["uuid"])
        is_admin = User.is_admin(session["uuid"])
        email = User.get_email_by_id(session["uuid"])
        reports = User.get_reports(_id)
        return view.render_template(view='reports.html',reports=reports,username=username,admin=is_admin,email=email)
    else:
        return redirect(url_for('index'))
@app.route('/logout',methods=['POST','GET'])
def logout():
	User.logout()
	return redirect(url_for('index'))
@app.route('/administration',methods=['GET','POST'])
def administration():
    if session['log_in']==True:
        return view.render_template(view='admin/admin.html')
    else:
        return redirect(url_for('index'))
@app.route('/addreport',methods=['GET','POST'])
def new_report():
    if session['log_in'] == True:
        if request.method == 'POST':          
            reportOwner = session['uuid']
            reportName = request.form['reportName']
            reportType = request.form['reportType']
            reportLevel = request.form['reportLevel']      
            AttackVector = request.form['AttackVector']
            reportDescription = request.form['reportDescription']
            getprivilege = request.form['getprivilege']
            AttackComplexity = request.form['AttackComplexity']
            if 'reportContent' in request.files :
                reportContent = request.files['reportContent']
                reportFile = reportContent.filename
                report = Report.register_report(reportOwner,reportName,reportType,reportDescription,reportLevel,AttackComplexity,AttackVector,getprivilege,reportFile,reportContent)     
        return view.render_template(view='add.html')
    return redirect(url_for('index'))
    '''if session['log_in']== True: 
        _id = session['uuid']
        username = User.get_username(session["uuid"])
        is_admin = User.is_admin(session["uuid"])
        email = User.get_email_by_id(session["uuid"])
        posts = User.get_reports(_id)
        return view.render_template(view='add.html',posts=posts,username=username,admin=is_admin,email=email)
    else:
        return redirect(url_for(index))'''
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['name']
        #TODO by houssem 1- sanatize data passed from user
        if  check_email(email) == True and check_password(password) == True  and check_username(username) == True :
            user = User.register(username,email,password)
            if user:
                return redirect(url_for('index'))
            return 'Account already exists!'
        else:
            return redirect(url_for('index'))
    if session.get('log_in') != None :
        if session['log_in'] == True and request.method== 'GET':
            return redirect(url_for('index'))       
    return view.render_template(view='register.html')
@app.route('/gotcha', methods=['GET'])
def found_you():
    #just a route to check if ip return func is running ===> returns 127.0.0.1 with no proxy
    return(ready_to_get_banned())

@app.errorhandler(404)
def not_found(error):
    return view.render_template(view='error.html'), 404
if __name__ == '__main__':
    app.secret_key = conf.SECRET_KEY
app.run(debug=conf.DEBUG)