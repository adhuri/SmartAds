from __future__ import print_function


class Event:
	def __init__(self, startTime, summary, description, geocoordinates, tagList):
		self.startTime = startTime
		self.eventName = summary
		self.description = description
		self.geocoordinates = geocoordinates
		self.tagList = tagList

	def printContents(self):
		print(self.startTime, self.eventName, self.description, self.geocoordinates, self.tagList);