import os
basedir = os.path.abspath(os.path.dirname(__file__))
class BaseConfig:
	"""base config"""
	SECRET_KEY = ''
	MONGO_URI='mongodb://localhost:27017/iset_bugbounty'
	DEBUG= True
	database_name= 'iset_bugbounty'
	UPLOAD_FOLDER='/core/uprep1'
	REPORT_LIMIT=5

class StaticVars:
	""" global vars to be passed"""
	SITE_NAME= 'BugBountyTN'
	SITE_URL= 'https://127.0.0.1:5000'


class Development_Config(BaseConfig):
	DEBUG = True
	BCRYPT_LOG_ROUNDS=4
	

