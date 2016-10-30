from __future__ import print_function
from sets import Set

class Tagger:
	TAGS_MAP = {'Gym': ['Health','Energy'], 'Trek': ['Food', 'Snacks'], 'Dinner': ['Restaurant']}

	ITEM_TAGS_MAP = {
		'Tuna': ['FOOD', 'SEAFOOD'], 
		'Peanut Butter' : ['FOOD'],
		'Butter' : ['FOOD', 'DAIRY'],
		'Milk' : ['FOOD', 'DAIRY'],
		'Bananas' : ['FOOD', 'FRUITS'],
		'Pepper' : ['FOOD', 'VEGETABLES'],
		'Jif' : ['FOOD'],
		'Asparagus' : ['FOOD', 'VEGETABLES'],
		'Broccoli' : ['FOOD', 'VEGETABLES'],
		'Carrots' : ['FOOD', 'VEGETABLES'],
		'Cauliflower' : ['FOOD', 'VEGETABLES'],
		'Celery' : ['FOOD', 'VEGETABLES'],
		'Corn' : ['FOOD', 'VEGETABLES'],
		'Cucumbers' : ['FOOD', 'VEGETABLES'],
		'Lettuce' : ['FOOD', 'VEGETABLES'],
		'Greens' : ['FOOD', 'VEGETABLES'],
		'Mushrooms' : ['FOOD', 'VEGETABLES'],
		'Onions' : ['FOOD', 'VEGETABLES'],
		'Peppers' : ['FOOD', 'VEGETABLES'],
		'Potatoes' : ['FOOD', 'VEGETABLES'],
		'Spinach' : ['FOOD', 'VEGETABLES'],
		'Squash' : ['FOOD', 'VEGETABLES'],
		'Zucchini' : ['FOOD', 'VEGETABLES'],
		'Tomatoes' : ['FOOD', 'VEGETABLES'],
		'Apples' : ['FOOD', 'FRUITS'],
		'Avocados' : ['FOOD', 'FRUITS'],
		'Berries' : ['FOOD', 'FRUITS'],
		'Cherries' : ['FOOD', 'FRUITS'],
		'Grapefruit' : ['FOOD', 'FRUITS'],
		'Grapes' : ['FOOD', 'FRUITS'],
		'Kiwis' : ['FOOD', 'FRUITS'],
		'Lemon' : ['FOOD', 'FRUITS'],
		'Limes' : ['FOOD', 'FRUITS'],
		'Melon' : ['FOOD', 'FRUITS'],
		'Nectarines' : ['FOOD', 'FRUITS'],
		'Oranges' : ['FOOD', 'FRUITS'],
		'Peaches' : ['FOOD', 'FRUITS'],
		'Pears' : ['FOOD', 'FRUITS'],
		'Plums' : ['FOOD', 'FRUITS'],
		'Butter' : ['FOOD', 'DAIRY'],
		'Margarine' : ['FOOD', 'DAIRY'],
		'Cottage cheese' : ['FOOD', 'DAIRY'],
		'Milk' : ['FOOD', 'DAIRY'],
		'Sour cream' : ['FOOD', 'DAIRY'],
		'Whipped cream' : ['FOOD', 'DAIRY'],
		'Yogurt' : ['FOOD', 'DAIRY'],
		'Bacon' : ['FOOD', 'MEATS'],
		'Sausage' : ['FOOD', 'MEATS'],
		'Beef' : ['FOOD', 'MEATS'],
		'Chicken' : ['FOOD', 'MEATS'],
		'Ground beef' : ['FOOD', 'MEATS'],
		'Turkey' : ['FOOD', 'MEATS'],
		'Ham' : ['FOOD', 'MEATS'],
		'Pork' : ['FOOD', 'MEATS'],
		'Hot dogs' : ['FOOD', 'MEATS'],
		'Lunchmeat' : ['FOOD', 'MEATS'],
		'Turkey' : ['FOOD', 'MEATS'],
		'Antiperspirant ' : ['PERSONAL CARE'],
		'Deodorant' : ['PERSONAL CARE'],
		'Bath soap ' : ['PERSONAL CARE'],
		'Hand soap' : ['PERSONAL CARE'],
		'Condoms ' : ['PERSONAL CARE'],
		'Cosmetics' : ['PERSONAL CARE'],
		'Cotton swabs ' : ['PERSONAL CARE'],
		'Balls' : ['PERSONAL CARE'],
		'Facial cleanser' : ['PERSONAL CARE'],
		'Facial tissue' : ['PERSONAL CARE'],
		'Feminine products' : ['PERSONAL CARE'],
		'Floss' : ['PERSONAL CARE'],
		'Hair gel ' : ['PERSONAL CARE'],
		'Spray' : ['PERSONAL CARE'],
		'Lip balm' : ['PERSONAL CARE'],
		'Moisturizing lotion' : ['PERSONAL CARE'],
		'Mouthwash' : ['PERSONAL CARE'],
		'Razors ' : ['PERSONAL CARE'],
		'Shaving cream' : ['PERSONAL CARE'],
		'Shampoo ' : ['PERSONAL CARE'],
		'Conditioner' : ['PERSONAL CARE'],
		'Sunblock' : ['PERSONAL CARE'],
		'Toilet paper' : ['PERSONAL CARE'],
		'Toothpaste' : ['PERSONAL CARE'],
		'Vitamins ' : ['PERSONAL CARE'],
		'Supplements' : ['PERSONAL CARE']
	}

	@staticmethod
	def getItemTags(stringToTag):
		words = stringToTag.split()
		tagSet = Set()
		for word in words:
			if word in Tagger.ITEM_TAGS_MAP:
				tags = Tagger.ITEM_TAGS_MAP[word]
				for x in tags:
					tagSet.add(x)
		return list(tagSet)

	@staticmethod
	def getTags(stringToTag):
		tagList = []
		words = stringToTag.split()
		for word in words:
			if word in Tagger.TAGS_MAP :
				tagList += Tagger.TAGS_MAP[word]
		return tagList

# Example
# print(Tagger.getItemTags('Bananas and Bacon'))
# returns ['FOOD', 'MEATS', 'FRUITS']