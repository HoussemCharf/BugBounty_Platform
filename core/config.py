import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:@localhost'
database_name= 'iset_bugbounty'

class BaseConfig:
	"""global vars and base config"""
	SECRET_KEY = os.getenv('SECRET_KEY','bugsbunny@bounty')
	DEBUG= False
	BCRYPT_LOG_ROUNDS = 15
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development_Config(BaseConfig):
	"""development config for me and souheil"""
	DEBUG = True
	BCRYPT_LOG_ROUNDS=4
	SQLALCHEMY_TRACK_MODIFICATIONS=postgres_local_base + database_name