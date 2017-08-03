
from datetime import datetime

class A(object):
	def __init__(self, dateTime=None):
		self.time = datetime.now() if dateTime is None else dateTime
		print self.time

A(dateTime='2017-02-12 10:12:12')
