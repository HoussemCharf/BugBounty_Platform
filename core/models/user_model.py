import jwt
import datetime

from BugBounty_Platform.core.models import blacklisted
from BugBounty_Platform.core import app, db, bcrypt


class User(db.Model):
	""" user Model for storing user related details """
	__tablename__="users"

	# table structure aka fields
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	email = db.Column(db.String(255),unique=True,nullable=False)
	password = db.Column(db.String(255),nullable=False)
	role = db.Column(db.String(50),nullable=False,default='user')
	registered_on = db.Column(db.DateTime,nullable=False)
	admin = db.Column(db.Boolean,nullable=False,default=False)


	def __init__(self,email,password,role,admin=False):
		self.email=email
		self.password = bcrypt.generate_password_hash(password,app.config.get('BCRYPT_LOG_ROUNDS')).decode()
		self.role=role
		self.registered_on=datetime.datetime.now()
		self.admin=admin

	def encode_auth_token(self,user_id):
		""" generate the auth token :return string:"""
		try:
			payload={
				'exp':datetime.datetime.now()+datetime.timedelta(days=0,seconds=10),
				'iat':datetime.datetime.now(),
				'sub':user_id
			}
			return jwt.encode(payload,app.config.get('SECRET_KEY'),algorithm='HS256')
		except Exception as e:
			return e
	@staticmethod
	def decode_auth_token(auth_token):
		""" validate the auth token :return int or a string: takes auth token as a parm"""
		try:
			payload = jwt.decode(auth_token,app.config.get('SECRET_KEY'))
			is_blacklisted_token =BlacklistToken.check_blacklist(auth_token)
			if is_blacklisted_token:
				return 'Token Blacklisted, Login again'
			else:
				return payload['sub']
		except jwt.ExpiredSignatureError:
			return 'Session expired, please login again'
		except jwt.InvalidTokenError:
			return 'invalid session, please login again'
