from Store import *

class Offer:
	offerList = []
	def __init__(self, store, name, description, tags, userId = -1):
		self.store = store
		self.name = name
		self.description = description
		self.userId = userId
		self.tags = tags

	@staticmethod
	def populateOfferList():
		dummyOfferList = [['Offer 1',' Desc 1', ['Restaurant']],
		['Offer 2','Desc 2',['Food','Tuna']],
		['Offer 3', 'Desc 3', ['Food', 'Twinkies']],
		['Gatorade Offer!', 'Buy one get one Gatorade Free at 6 Twelve Convenient Store', ['Energy' , 'Health' , 'Gatorade']]]

		Store.populateStoreList()
		storeList = Store.storeList
		for offer in dummyOfferList:
			store = storeList[1]
			offerObj = Offer(store, offer[0], offer[1], offer[2], 20)
			Offer.offerList.append(offerObj)
