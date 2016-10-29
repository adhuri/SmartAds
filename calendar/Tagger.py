from __future__ import print_function

class Tagger:
	TAGS_MAP = {'Gym': ['Health','Energy'], 'Trek': ['Food', 'Snacks'], 'Dinner': ['Restaurant']}
	
	@staticmethod
	def getTags(stringToTag):
		words = stringToTag.split()
		for word in words:
			if word in Tagger.TAGS_MAP :
				print(Tagger.TAGS_MAP[word])

