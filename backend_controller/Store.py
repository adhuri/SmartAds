from __future__ import print_function
from geopy.geocoders import *


class Store:
	storeList = []
	def __init__(self, name, address, geocordinatesList):
		self.name = name
		self.address = address
		self.geocordinatesList = geocordinatesList

	@staticmethod
	def populateStoreList():
		dummyStoreList = [['FoodLion','3415 Avent Ferry Rd Raleigh NC'],
		['Convinience Store','2109 Avent Ferry Rd Raleigh NC']]
		#print(dummyStoreList)
		for store in dummyStoreList:
			geolocator = ArcGIS()
			coordinates = geolocator.geocode(store[1])
			#print(store[1])
			geocoordinates = [coordinates.latitude, coordinates.longitude]
			storeObj = Store(store[0], store[1], geocoordinates)
			Store.storeList.append(storeObj)
		
	def printContents(self):
		print(self.name, self.address, self.geocordinatesList);

		