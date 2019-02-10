import os
basedir = os.path.abspath(os.path.dirname(__file__))
class BaseConfig:
	"""base config"""
	SECRET_KEY = 'bugsbunny@bounty'
	MONGO_URI='mongodb://localhost:27017/iset_bugbounty'
	DEBUG= False
	database_name= 'iset_bugbounty'

class StaticVars:
	""" global vars to be passed"""
	SITE_NAME= 'BugBounty Platform'
	SITE_URL= 'https://isetcom.tn'
class Development_Config(BaseConfig):
	"""development config for me and souheil"""
	DEBUG = True
	BCRYPT_LOG_ROUNDS=4
	

