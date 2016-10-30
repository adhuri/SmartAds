class Offer:
	def __init__(self, store, description, userId = -1, tags):
		self.store = store
		self.description = description
		self.userId = userId
		self.tags = tags

	def populateOfferList():
		dummyStoreList = [['Offer 1',' Desc 1', ['Restaurant']],
		['Offer 2','Desc 2',['Food','Tuna']],
		['Offer 3', 'Desc 3', ['Food', 'Twinkies']],
		['Offer 4', 'Desc 4', ['Energy' , 'Health' , 'Gatorade']]]

		for store in dummyStoreList:
			geolocator = Nominatim()
			coordinates = geolocator.geocode(store[1])
			#print(store[1])
			geocoordinates = [coordinates.latitude, coordinates.longitude]
			storeObj = Store(store[0], store[1], geocoordinates)
			Store.storeList.append(storeObj)
