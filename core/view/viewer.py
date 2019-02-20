from flask import render_template,session,url_for,redirect
from config import StaticVars as static_vars
from config import BaseConfig as conf

class view(object):
	@staticmethod
	def render_template(view,session=session,static_vars=static_vars,error=None,**kwargs):
		return render_template(view,session=session,static_vars=static_vars,error=error,**kwargs)