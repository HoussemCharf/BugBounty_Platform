import re
from flask import session
from flask import request,redirect,url_for
from models.Usermodel import User

def check_form_empty(form):
	values = form.values()
	for x in values:
		if len(x)==0:
			return True
	return False
def secure_file_name(filename):
	_id = session['uuid']
	dotexploded=filename.split('.')
	cyphered = dotexploded[0]+_id[:5]+dotexploded[len(dotexploded)-1]
	return cyphered
def check_email(email):
	#regex is updatable to the needs"
	if not re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$",email):
		return False
	return True
def check_password(password):
	  #regex is updatable to the needs"
	if not re.match("^\w{7,15}$",password):
		return False
	return True
def check_username(username):
	if not re.match("^[\w]{6,15}$",username):
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
