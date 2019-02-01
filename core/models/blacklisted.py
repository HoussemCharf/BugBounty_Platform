import jwt
import datetime

from BugBounty_Platform.core import app, db, bcrypt

class BlacklistedToken(db.Model):
	""" Token model for storing jwt tokens"""

	__tablename__ = 'blacklist_tokens'

	# structure aka fields

	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	token = db.Column(db.String(500),unique=True,nullable=False)
	blacklisted_on = db.Column(db.DateTime,nullable=False)


	def __init__(self,token):
		self.token=token
		self.blacklisted_on=datetime.datetime.now()

	def __repr__(self):
		return '<id: token:{}'.format(self.token)

	@staticmethod
	def check_blacklist(auth_token):
		# query to check if a token blacklisted or not
		check = BlacklistedToken.query.filter_by(token=str(auth_token)).first()
		if check:
			return True
		else:
			return False