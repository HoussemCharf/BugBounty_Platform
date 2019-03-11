import uuid
import datetime
from flask import session
from utils.Database import Database
import bcrypt
from  models.ReportModel import Report
class User(object):
	def __init__(self,username,email,password,firstpartner,secondpartner,_id=None,registeredOn=None,admin=False):
		self.username = username
		self.email = email
		self.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
		self.firstpartner = firstpartner
		self.secondpartner = secondpartner 
		self._id = uuid.uuid4().hex if _id is None else _id
		self.registeredOn=datetime.datetime.now()
		self.admin = admin
	@classmethod
	def get_by_email(cls,email):
		# get user by filling email
		data = Database.find_one("users",{"email":email})
		if data is not None:
			return data
	@classmethod
	def get_password_hash(cls,email):
		data = Database.find_one("users",{"email":email})
		if data is not None:
			return data["password"]
	@classmethod
	def get_by_id(cls,_id):
		data = Database.find_one("users",{"_id":_id})
		if data is not None:
			return data
	@classmethod
	def get_id_by_email(cls,email):
		data = Database.find_one("users",{"email":email})
		return data["_id"]
	@classmethod	
	def get_username(cls,_id):
		data = cls.get_by_id(_id)
		return data["username"]
	@classmethod
	def get_only_email(self,email):
		data =Database.find_one("users",{"email":email})
		if data is not None:
			return data['email']
		else:
			return None
	@classmethod
	def get_email_by_id(cls,_id):
		data = cls.get_by_id(_id)
		return data["email"]
	@classmethod
	def valid_login(cls,email,password):
		#context needed here!
		user = cls.get_by_email(email)
		if user is not None:
			return bcrypt.checkpw(password.encode("utf-8"),user["password"])
		return False
	@classmethod
	def register(cls,username,email,password,firstpartner,secondpartner):
		user = cls.get_only_email(email)
		if user is None:
			guest = cls (username,email,password,firstpartner,secondpartner)
			guest.savemongo()
			dataSaved = cls.get_by_email(email)
			cls.init_login(dataSaved["_id"])
			return True
		else:
			return False
	@classmethod
	def login(cls,_id):
		cls.init_login(_id)
	@classmethod
	def is_admin(cls,_id):
		data = cls.get_by_id(_id)
		return data["admin"]==True
	@classmethod
	def logout(cls):
		session["uuid"] = None
		session['log_in'] =False
	@classmethod
	def init_login(self,_id):
		session['log_in'] = True
		session['uuid']=_id
	@classmethod
	def get_reports(self,_id):
		return Report.find_reports_by_owner_id(_id)
	@staticmethod
	def count_users():
		data = Database.find("users",{})
		if data is not None:
			return data.count()
	@classmethod
	def update(self,_id,field,value):
		self.updatemongo(self.update_json(_id,field,vlaue))
	def json(self):
		return {
		"username":self.username,
		"email":self.email,
		"_id":self._id,
		"password":self.password,
		"admin":self.admin,
		"registeredOn":self.registeredOn,
		"firstpartner" : self.firstpartner,
		"secondpartner" : self.secondpartner
		}
	def update_json(self,_id,field,value):
		return {"_id":_id},{
				"$set":{
					field:value
				}
			}
	def savemongo(self):
		Database.insert("users",self.json())
	def updatemongo(self,query):
		Database.update("users",query)
