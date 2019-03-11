from flask import render_template,session,url_for,redirect
from config import StaticVars as static_vars
from config import BaseConfig as conf
from models.Usermodel import User
class view(object):
	@staticmethod
	def render_template(view,session=session,static_vars=static_vars,error=None,success=None,**kwargs):
		username=None
		is_admin=False
		email=None
		if session.get('log_in') != None: 
			if session['log_in'] == True:
				_id=session['uuid']
				username = User.get_username(_id)
				is_admin = User.is_admin(_id)
				email = User.get_email_by_id(_id)
		return render_template(view,session=session,static_vars=static_vars,username=username,admin=is_admin,email=email,error=error,success=success,**kwargs)