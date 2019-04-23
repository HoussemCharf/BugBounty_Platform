import re
from flask import session
from flask import request,redirect,url_for
from models.Usermodel import User
from models.ReportModel import Report
from models.ChatModel import Chat
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
def get_chat_messages(_id):
	#i cri everytim
	legacy = []
	data = Chat.get_user_initial_messages(_id)
	if data:
		message = list(data)
		for x in range(0,len(message)):
			new_data = message[x]['messageId']
			content_data = message[x]
			legacy.append(content_data)
			admin_message = Chat.get_user_message_by_replymessageId(new_data)
			if admin_message:
				legacy.append(admin_message)
		return legacy
def get_username_from_messages(data):
	names = []
	if data is not None:
		for x in range(len(data)):
			messageOwners = data[x]['messageOwner']
			name = User.get_username(messageOwners)
			names.append(name)
		return names
