import os
basedir = os.path.abspath(os.path.dirname(__file__))
class BaseConfig:
	"""global vars and base config"""
	SECRET_KEY = 'bugsbunny@bounty'
	MONGO_URI='mongodb://localhost:27017/iset_bugbounty'
	DEBUG= False
	database_name= 'iset_bugbounty'

class Development_Config(BaseConfig):
	"""development config for me and souheil"""
	DEBUG = True
	BCRYPT_LOG_ROUNDS=4
	

