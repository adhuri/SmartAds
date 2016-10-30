from __future__ import print_function
from Offer import *
from Store import *
from calendarApi import *

def getCalendarBasedOffer():
	eventList = getEventsForUser()
	#print(eventList)
	Offer.populateOfferList()
	offerList = Offer.offerList
	#print(offerList)
	customerOffer = []
	for event in eventList:
		for tags in event.tagList:
			for offer in offerList:
				if tags in offer.tags :
					customerOffer.append(offer)
	return list(set(customerOffer))



#print(getCalendarBasedOffer());