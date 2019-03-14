from datetime import datetime
import uuid
from flask import session
from utils.Database import Database as base
from bson.objectid import ObjectId
class Notification(object):
	def __init__ (self,notiId,notiTitle,notiDescription,notiDate,notiOwner,notiViewed=False):
		self.notiId = uuid.uuid4().hex if reportId is None else reportId
		self.notiTitle = notiTitle
		self.notiDescription = notiDescription
		self.notiDate = datetime.now()
		self.notiViewed = notiViewed
		self.notiOwner= notiOwner
	@classmethod
	def get_notification_by_id(cls,notiId):
		data = base.find_one("notification",{"notiId":reportId})
		if data is not None:
			return data
	@classmethod
	def get_notifications_by_owner_id(cls,notiOwner):
		data = base.find("notification",{"notiOwner":notiOwner})
		if data is not None:
			return list(data)
	def json(self):
		return {
		"notiId":self.notiId,
		"notiTitle":self.notiTitle,
		"notiDescription":self.notiDescription,
		"notiDate":self.notiDate,
		"notiView":self.notiViewed,
		"notiOwner":self.notiOwner,
		}
	def savemongo(self):
		Database.insert("notification",self.json())