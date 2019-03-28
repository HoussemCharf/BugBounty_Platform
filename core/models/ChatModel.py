from datetime import datetime
import uuid
from flask import session
from utils.Database import Database
class Chat(object):
	def __init__ (self,messageOwner,messageContent,messageOwnerName,responsemessage=None,responseAdmin=None,responsemessageDate=None,messageDate=None,messsageId=None):
		self.messageId = uuid.uuid4().hex if messsageId is None else messageId
		self.messageOwner = messageOwner
		self.messageOwnerName = messageOwnerName
		self.messageDate = datetime.now()
		self.messageContent = messageContent
		self.responsemessage = responsemessage
		self.responsemessageDate = responsemessageDate
		self.responseAdmin = responseAdmin

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
	def register_message(cls,messageOwner,messageContent,messageOwnerName):
		unsavedmessage =cls(messageOwner,messageContent,messageOwnerName)
		if unsavedmessage is not None:
			unsavedmessage.save()
	def json(self):
		return{
		"messageId":self.messageId,
		"messageOwner":self.messageOwner,
		"messageOwnerName":self.messageOwnerName,
		"messageDate":self.messageDate,
		"messageContent": self.messageContent,
		"responseAdmin" : self.responseAdmin,
		"responsemessage" : self.responsemessage,
		"responsemessageDate" : self.responsemessageDate}
	def save(self):
		Database.insert("chat",self.json())
		