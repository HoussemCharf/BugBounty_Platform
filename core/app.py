from flask import Flask, render_template, url_for, request, session, redirect
from config import BaseConfig as conf
from config import StaticVars as static_vars
from utils.Database import Database as base
from utils.sanatize import *
from models.Usermodel import User
from models.ReportModel import Report 
from view.viewer import view
import os
import datetime

app = Flask(__name__)

@app.before_first_request
def initial():
	base.initialize()
@app.route('/')
def index():
    # if user is logged in setting up vars to be used in rendering the index template
    if session.get('log_in') != None: 
        if session['log_in'] == True:
            _id=session['uuid']
            return view.render_template(view='home.html')
    return view.render_template(view='home.html')
@app.route('/auth',methods=['GET'])
def auth():
    return view.render_template(view='auth.html') 
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        error = None
        email= request.form['email']
        password = request.form['password']
        #TODO by Houssem 1- sanatize data passed from user
        if User.valid_login(email,password):
        # Hacky code here <.<
            uuid = User.get_id_by_email(email)
            User.login(uuid)
            return redirect(url_for('index'))
        else:
            error ='Wrong credentials please verify your informations'
    return view.render_template(view='auth.html',error=error)
@app.route('/reports',methods=['GET'])
def reports():
    if session['log_in'] == True:
        _id = session['uuid']
        reports = User.get_reports(_id)
        length = len(reports)
        return view.render_template(view='reports.html',reports=reports,length=length)
    else:
        return redirect(url_for('index'))
@app.route('/logout',methods=['POST','GET'])
def logout():
	User.logout()
	return redirect(url_for('index'))
@app.route('/administration/ban',methods=['GET'])
def ban_redirect():
    if session['log_in']==True:
        _id= session['uuid']
        if User.is_admin(_id):
            banned_user=request.args['id']
            User.update(banned_user,'banned',True)
            return redirect(url_for('administration'))
        else:
            User.update(_id,'banned',True)
    return redirect(url_for('index'))
@app.route('/administration/scorerep',methods=['POST'])
def score_report():
    if session['log_in']==True:
        _id= session['uuid']
        if User.is_admin(_id):
            edit_report=request.form['id']
            score=request.form['score']
            res=Report.set_score(edit_report,score)
            if res:
                success="scored successfully!"
                return view.render_template(view='/admin/admin.html',success=success)
            else:
                error="Ops, something went wrong!"
                return view.render_template(view='/admin/admin.html',error=error)
        else:
            User.update(_id,'banned',True)
    return redirect(url_for('index'))
@app.route('/administration/editreport',methods=['GET'])
def evaluate_report():
    if session['log_in']==True:
        _id= session['uuid']
        if User.is_admin(_id):
            edit_report=request.args['id']
            report=Report.get_report(edit_report)
            if report['locked']== False:
                return view.render_template(view='admin_report.html',report=report)
            else:
                error="Another admin is currently evaluating!"
                return view.render_template(view='/admin/admin.html',error=error)
        else:
            User.update(_id,'banned',True)
    return redirect(url_for('index'))
@app.route('/administration',methods=['GET','POST'])
def administration():
    if session['log_in']==True:
        _id = session['uuid']
        if User.is_admin(_id):
        # counting reports and users
            countReports = Report.get_all_reports_count()
            countUsers = User.count_users()
            # count waiting submissions
            pendingReportsCount = Report.get_pending_reports_count()
            acceptedReportsCount = Report.get_accepted_reports_count()
            rejectedReportsCount = Report.get_rejected_reports_count()
            acceptedReportsRatio = round(acceptedReportsCount * 100 / countReports)
            currentDate=datetime.datetime.now()
            # this section gonna deal with the users management view in the admin dashboard
            allUsers=User.get_all_users()

            # this section gonna deal with the reports management view in the admin dashboard
            allReports = Report.get_all_reports()
            allPending = Report.get_all_pending_reports()
            allAccepted = Report.get_all_accepted_reports()
            allRejected = Report.get_all_rejected_reports()
            # this section gonna handle the mini leaderboard in the admin panel
            Ranking=[]
            for user in allUsers:
                print(user)
                if user['admin'] == True:
                    pass
                else:
                    Ranking.append(calculate_score_for_user(user))
            sorted(Ranking,key=lambda l:l[1])
            length=len(Ranking)
            print(length)
            return view.render_template(view='admin/admin.html',countReports=countReports,countUsers=countUsers,pendingReportsCount=pendingReportsCount,acceptedReportsCount=acceptedReportsCount,rejectedReportsCount=rejectedReportsCount,ratio=acceptedReportsRatio,
                allReports=allReports,allUsers=allUsers,allPending=allPending,allAccepted=allAccepted,allRejected=allRejected,currenttime=currentDate
                ,length=length,ranking=Ranking)
    return redirect(url_for('index'))
@app.route('/settings', methods=['GET','POST'])
def settings():
    if session['log_in']==True:
        success=None
        error=None
        if request.method=='POST':
            _id = session['uuid']
            Newpassword = request.form['password']
            if check_password(Newpassword) and Newpassword!=None:
                User.update(_id,"password",Newpassword)
                success = "Password changed successfully!"
            else:
                error = "Ops, Something wrong happened!"
            return view.render_template(view='settings',success=success,error=error)
        return view.render_template(view='settings.html')
    else:
        return redirect(url_for('settings'))
@app.route('/addreport',methods=['GET','POST'])
def new_report():
    if session['log_in'] == True:
        _id = session['uuid']
        if request.method == 'POST':
            if check_form_empty(request.form,ignore='reportContent'):
                error='Please fill all the form before submiting!'
                return view.render_template(view='add.html',error=error)
            else:
                reportOwner =_id
                reportName =request.form['reportName']
                reportType =request.form['reportType']
                reportLevel =request.form['reportLevel']      
                AttackVector =request.form['AttackVector']
                reportDescription =request.form['reportDescription']
                getprivilege =request.form['getprivilege']
                AttackComplexity =request.form['AttackComplexity']
            # handle file upload section
                if 'reportContent' in request.files:
                    file =request.files['reportContent']
                else:
                    file = False
                reportFile = None
                if Report.get_reports_queue(_id)<=conf.REPORT_LIMIT:
                    if file:
                        reportFile = secure_file_name(file.filename)
                        file.save(os.path.join(os.getcwd()+conf.UPLOAD_FOLDER,reportFile))
                    report = Report.register_report(reportOwner,reportName,reportType,reportDescription,reportLevel,AttackComplexity,AttackVector,getprivilege,reportFile)
                    success = 'Reported submitted successfully!'
                    return view.render_template(view='add.html',success=success)
                else:
                    error='Due to flooding threat every user is limited to only '+str(conf.REPORT_LIMIT)+' reports in pending queue, Sorry for the inconvenience.'
                    return view.render_template(view='add.html',error=error)
        elif request.method == 'GET':
            user = User.get_by_id(_id)
            error = None
            if user['banned'] == True:
                error = "You are not allowed, to add a report because you are banned!"
                return view.render_template(view='banned.html',error=error)
            return view.render_template(view='add.html',error=error)
    return redirect(url_for('index'))
@app.route('/register', methods=['POST','GET'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['name']
        firstpartner = request.form['firstpartner']
        secondpartner = request.form['secondpartner']
        thirdpartner = request.form['thirdpartner']
        #TODO by houssem 1- sanatize data passed from user
        if  check_email(email) == True and check_password(password) == True  and check_username(username) == True and check_firstpartner(firstpartner) == True and check_secondpartner(secondpartner) == True and check_thirdpartner(thirdpartner) == True:            
            user = User.register(username,email,password,firstpartner,secondpartner,thirdpartner)
            if user:
                return redirect(url_for('index'))
            error= 'Account already exists!'
            return view.render_template(view='register.html',error=error)
        else:
            error = 'Invalid input, please verify again'
    if session.get('log_in') != None :
        if session['log_in'] == True and request.method== 'GET':
            return redirect(url_for('index'))       
    return view.render_template(view='register.html',error=error)
@app.route('/gotcha', methods=['GET'])
def found_you():
    #just a route to check if ip return func is running ===> returns 127.0.0.1 with no proxy
    return(ready_to_get_banned())
@app.route('/leaderboard')
def leaderboard():
        # add lock here from admin settings
    allUsers=User.get_all_users()
    Ranking=[]
    for user in allUsers:
        if user['admin']== True or user['banned'] == True:
            pass
        else:
            Ranking.append(calculate_score_for_user(user))
    sorted(Ranking,key=lambda l:l[1])
    length=len(Ranking)
    return view.render_template(view='leaderboard.html',ranking=Ranking,length=length)

@app.errorhandler(404)
def not_found(error):
    return view.render_template(view='error.html'), 404
if __name__ == '__main__':
    app.secret_key = conf.SECRET_KEY
app.run(ssl_context='adhoc',port=5000,debug=conf.DEBUG)