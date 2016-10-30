from __future__ import print_function

class Tagger:
	TAGS_MAP = {'Gym': ['Health','Energy'], 'Trek': ['Food', 'Snacks'], 'Dinner': ['Restaurant']}

	@staticmethod
	def getTags(stringToTag):
		tagList = []
		words = stringToTag.split()
		for word in words:
			if word in Tagger.TAGS_MAP :
				tagList += Tagger.TAGS_MAP[word]
		return tagList

