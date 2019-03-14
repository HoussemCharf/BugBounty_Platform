import re
from flask import session
from flask import request,redirect,url_for
from models.Usermodel import User
from models.ReportModel import Report
from werkzeug.utils import secure_filename
import random
import string
import bcrypt
ALLOWED_EXTENSIONS = set(['pdf'])

secure_string = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
def check_form_empty(form,ignore=None):
	values = form.keys()
	if form.get(ignore) is not None:
		values=list(values)
		values.remove(ignore)
	for x in values:
		if len(form[x])==0:
			return True
	return False
#Lambda expression MAN I AM in love <3

	# tobecontinued
def secure_file_name(filename):
	_id = session['uuid']
	dotexploded=filename.split('.')
	cyphered = secure_string(10)+'.'+dotexploded[len(dotexploded)-1]
	return secure_filename(cyphered)
def check_email(email):
	#regex is updatable to the needs"
	if not re.match("^\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+$",email):
		return False
	return True
def general_check(str1,borninf,bornsup):
	if not re.match("^[\w]{"+str(borninf)+","+str(bornsup)+"}$",str1):
		return False
	return True
def ready_to_get_banned():
		#no proxy involved
	if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
		return(request.environ['REMOTE_ADDR'])
		#proxy involved
	else:
		return(request.environ['HTTP_X_FORWARDED_FOR'])
	return ('you have no connected IPs')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
