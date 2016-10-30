from __future__ import print_function
from geopy.geocoders import Nominatim


class Store:
	storeList = []
	def __init__(self, name, address, geocordinatesList):
		self.name = name
		self.address = address
		self.geocordinatesList = geocordinatesList

	@staticmethod
	def populateStoreList():
		dummyStoreList = [['FoodLion','3415 Avent Ferry Rd Raleigh NC'],
		['Crossroads Chapel Hill','211 Pittsboro St Chapel Hill NC'],
		['David\'s Dumpling & Noodle Bar', '1900 Hillsborough St Raleigh NC'],
		['Char-Grill', '618 Hillsborough St Raleigh NC']]
		#print(dummyStoreList)
		for store in dummyStoreList:
			geolocator = Nominatim()
			coordinates = geolocator.geocode(store[1])
			#print(store[1])
			geocoordinates = [coordinates.latitude, coordinates.longitude]
			storeObj = Store(store[0], store[1], geocoordinates)
			Store.storeList.append(storeObj)

		#FoodLion
		#Crossroads Chapel Hill 
		#David's Dumpling & Noodle Bar
		#Char-Grill
	def printContents(self):
		print(self.name, self.address, self.geocordinatesList);


def main():
    Store.populateStoreList()
    for store in Store.storeList:
    	store.printContents()

if __name__ == '__main__':
    main()  
		