import uuid
import datetime
from flask import session
from utils.Database import Database
import bcrypt

class User(object):
	def __init__(self,username,email,password,_id=None,registeredOn=None,admin=False):
		self.username = username
		self.email = email
		self.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
		self._id = uuid.uuid4().hex if _id is None else _id
		self.registeredOn=datetime.datetime.now()
		self.admin = admin
	@classmethod
	def get_by_email(cls,email):
		# get user by filling email
		data = Database.find_one("users",{"email":email})
		if data is not None:
			return cls(**data)
	@classmethod
	def get_by_id(cls,_id):
		data = Database.find_one("users",{"_id":_id})
		if data is not None:
			return cls(**data)
	@classmethod
	def get_id_by_email(cls,email):
		data = cls.get_by_email(email)
		return data["_id"]
	@classmethod
	def get_username(cls,_id):
		data = cls.get_by_id(_id)
		return data["username"]
	@classmethod
	def valid_login(cls,email,password):
		user = cls.get_by_email(email)
		if user is not None:
			return user.password == bcrypt.hashpw(password.encode('utf-8'))
		return False
	@classmethod
	def register(cls,username,email,passw):
		user = cls.get_by_email(email)
		if user is None:
			print(type(passw))
			print(passw)
			guest = cls(username,email,passw)
			guest.savemongo()
			dataSaved = cls.get_by_email(email)
			session["uuid"] = dataSaved["_id"]
			print(True)
			return True
		else:
			return False
	@classmethod
	def login(_id):
		session['log_in'] = True
		session['uuid']=_id
	@classmethod
	def is_admin(cls,_id):
		data = cls.get_by_id(_id)
		return data["admin"]==True
	@classmethod
	def logout():
		session["uuid"] = None
		session['log_in'] =False
	def json(self):
		return {
		"username":self.username,
		"email":self.email,
		"_id":self._id,
		"password":self.password,
		"admin":self.admin,
		"registeredOn":self.registeredOn
		}
	def savemongo(self):
		Database.insert("users",self.json())