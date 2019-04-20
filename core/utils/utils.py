import re
from flask import session
from flask import request,redirect,url_for
from models.Usermodel import User
from models.ReportModel import Report
from werkzeug.utils import secure_filename
import random
import string
import bcrypt


def calculate_score_for_user(user):
	score=0
	if user['banned']==False:
		allUserReports=Report.find_reports_by_owner_id(user['_id'])
		for report in allUserReports:
			score+=int(report['reportScore'])
	return[user['username'],score]
def compare_strings(str1,str2):
	return str1 == str2
def password_check(currentpassword,basePassword):
	return bcrypt.checkpw(currentpassword.encode("utf-8"),basePassword)
def hashpass(password):
	return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
def get_username(report):
	user = report['reportOwner']
	if user is not None:
		username = User.get_by_id(user)
		return username['username']
def get_username_from_message(message):
	user = message['messageOwner']
	if user is not None:
		username = User.get_by_id(user)
		return username['username']
def get_reports_per_user_count(_id):
	post = Report.find_reports_by_owner_id(_id)
	if post is not None:
		return len(post)
