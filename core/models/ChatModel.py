from datetime import datetime
import uuid
from flask import session
from utils.Database import Database
class Chat(object):
	def __init__ (self,messageOwner,messageContent,replymessageId=None,messageDate=None,messageId=None,instantMessage=0):
		self.messageId = uuid.uuid4().hex if messageId is None else messageId
		self.messageOwner = messageOwner
		self.messageDate = datetime.now()
		self.messageContent = messageContent
		self.replymessageId = replymessageId
		self.instantMessage = instantMessage
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
	def get_instant_messages():
		data = Database.find("chat",{"instantMessage" : {"$eq": 1}})
		if data is not None:
			return data		
	@classmethod
	def register_message(cls,messageOwner,messageContent):
		unsavedmessage =cls(messageOwner,messageContent)
		if unsavedmessage is not None:
			unsavedmessage.save()
	@classmethod
	def update(self,_id,field,value):
		base.update("chat",{"filter":{"messageOwner":_id},"update":{"$set":{field:value}}})
	def json(self):
		return{
		"messageId":self.messageId,
		"messageOwner":self.messageOwner,
		"messageDate":self.messageDate,
		"messageContent": self.messageContent,
		"replymessageId" :self.replymessageId,
		"instantMessage" : self.instantMessage}
	def save(self):
		Database.insert("chat",self.json())
		