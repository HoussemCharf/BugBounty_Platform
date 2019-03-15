from flask_pymongo import pymongo
from config import BaseConfig as conf


class Database(object):
	URI = conf.MONGO_URI
	@staticmethod
	def initialize():
		client = pymongo.MongoClient(Database.URI)
		Database.DATABASE = client[conf.database_name]
	@staticmethod
	def insert(collection,data):
		Database.DATABASE[collection].insert(data)
	@staticmethod
	def find(collection,query):
		return Database.DATABASE[collection].find(query)
	@staticmethod
	def find_one(collection,query):
		return Database.DATABASE[collection].find_one(query)
	@staticmethod
	def update(collection,query):
		return Database.DATABASE[collection].update_one(query['filter'],query['update'])
	@staticmethod
	def delete(collection,query):
		return Database.DATABASE[collection].delete_one(query)