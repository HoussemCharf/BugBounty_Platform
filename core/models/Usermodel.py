import uuid
import datetime
from flask import session
import bcrypt

class User(object):
	def __init__(self,email,password,_id=None):
		self.email=email
		self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		self._id = uuid.uuid4().hex if _id is None else _id

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
	def valid_login(email,password):
		user = User.get_by_email(email)
		if user is not None:
			return user.password == bcrypt.hashpw(password.encode('utf-8'))
		return False

	@classmethod
	def register(cls,email,password):
		user = cls.get_by_email(email)
		if user is None:
			guest = cls(email,password)
			guest.savemongo()
			session["email"] = email
			return True
		else:
			return False
	@classmethod
	def login(email):
		session["email"] = email
	@classmethod
	def logout():
		session["email"] = None
	def json(self):
		return {
		"email":self.email,
		"_id":self._id,
		"password":self.password
		}
	def savemongo(self):
		Database.insert("users",self.json())