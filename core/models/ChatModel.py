from datetime import datetime
import uuid
from flask import session
from utils.Database import Database
class Chat(object):
	def __init__ (self,messageOwner,messageContent,replymessageId,instantMessage,viewed,messageDate=None,messageId=None):
		self.messageId = uuid.uuid4().hex if messageId is None else messageId
		self.messageOwner = messageOwner
		self.messageDate = datetime.now()
		self.messageContent = messageContent
		self.replymessageId = replymessageId
		self.instantMessage = instantMessage
		# if admin message viewed = -1 , 1 for viewed user messages and 0 for non viewed user messages.
		self.viewed = viewed
	@staticmethod
	def get_all_messages():
		data = Database.find("chat", {})
		if data is not None:
			return list(data)
	@classmethod
	def get_message_by_messageOwner(cls,owner):
		data = Database.find("chat",{"messageOwner" : owner})
		if data is not None:
			return list(data)
	@classmethod
	def get_message_byDate(cls,messageDate):
		data = Database.find("chat",{"messageDate" : messageDate})
		if data is not None:
			return list(data)
	@staticmethod
	def get_instantadmin_messages():
		data = Database.find("chat",{"instantMessage" : {"$eq": 1}})
		if data is not None:
			return list(data)
	@staticmethod
	def get_allusers_messages():
		data = Database.find("chat",{"instantMessage" : {"$eq": 0}})
		if data is not None:
			return list(data)
	@staticmethod
	def get_unviewed_messages():
		data = Database.find("chat",{"viewed" : {"$eq" : 0}})
		if data is not None:
			return list(data)
	@classmethod
	def get_message(cls,messageId):
		data = Database.find_one("chat",{"messageId":messageId})
		if data is not None:
			return data		
	@classmethod
	def register_message(cls,messageOwner,messageContent,replymessageId,instantMessage,viewed):
		unsavedmessage =cls(messageOwner,messageContent,replymessageId,instantMessage,viewed)
		if unsavedmessage is not None:
			unsavedmessage.save()
	@classmethod
	def update(self,_id,field,value):
		Database.update("chat",{"filter":{"messageId":_id},"update":{"$set":{field:value}}})
	@classmethod
	def delete(self,messageId):
		Database.delete("chat",{"messageId":messageId})
	def json(self):
		return{
		"messageId":self.messageId,
		"messageOwner":self.messageOwner,
		"messageDate":self.messageDate,
		"messageContent": self.messageContent,
		"replymessageId" :self.replymessageId,
		"instantMessage" : self.instantMessage,
		"viewed" : self.viewed}
	def save(self):
		Database.insert("chat",self.json())
		