from datetime import datetime
import uuid
from flask import session
from utils.Database import base
import bcrypt

class Report(object):
	def __init__ (self,reportId=None,reportName,reportType,reportDate=None,reportLevel,reportFile,reportContent,reportOwner,reportScore=0):
		self.reportId = uuid.uuid4().hex if _id is None else _id
		self.reportName = reportName
		self.reportType = reportType
		self.reportDate = datetime.now()
		self.reportLevel = reportLevel
		self.reportFile = reportFile
		self.reportContent = reportContent
		self.reportOwner = reportOwner
		self.reportScore = reportScore
	@classmethod
	def get_report_name(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportName']
	@classmethod
	def get_report_type(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportType']
	@classmethod
	def get_report_date(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportDate']
	@classmethod
	def get_report_level(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportLevel']
	@classmethod
	def get_report(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return cls(**data)
	@classmethod
	def set_score(cls,reportId,score):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			base.update_one("reports",reportId,"score",score)
			return True
		else:
			return False
	@classmethod
	def register_report(cls,reportName,reportType,reportLevel,reportFile,reportContent,reportOwner):
		#TODO fix report file saving
		try:
			unsavedReport = cls(reportName,reportType,reportLevel,reportFile,reportContent,reportOwner)
			unsavedReport.save_mongo()
			return True
		except:
			return False
	def json(self):
		return{
		"reportName":self.reportName,
		"reportType":self.reportType,
		"reportLevel":self.reportLevel,
		"reportFile":self.reportFile,
		"reportContent":self.reportContent,
		"reportOwner":self.reportOwner
		}
	def save_mongo(self):
		base.insert("reports",self.json)
