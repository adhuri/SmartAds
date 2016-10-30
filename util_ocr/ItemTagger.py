from __future__ import print_function
from sets import Set

class Tagger:
	ITEM_TAGS_MAP = {
		'TUNA': ['FOOD', 'SEAFOOD'], 
		'PEANUT BUTTER' : ['FOOD'],
		'BUTTER' : ['FOOD', 'DAIRY'],
		'MILK' : ['FOOD', 'DAIRY'],
		'BANANAS' : ['FOOD', 'FRUITS'],
		'PEPPER' : ['FOOD', 'VEGETABLES'],
		'JIF' : ['FOOD'],
		'PB' : ['FOOD', 'SNACKS'],
		'LAYS' : ['FOOD', 'SNACKS'],
		'DORITOS' : ['FOOD', 'SNACKS'],
		'PRINGLES' : ['FOOD', 'SNACKS'],
		'ASPARAGUS' : ['FOOD', 'VEGETABLES'],
		'BROCCOLI' : ['FOOD', 'VEGETABLES'],
		'CARROTS' : ['FOOD', 'VEGETABLES'],
		'CAULIFLOWER' : ['FOOD', 'VEGETABLES'],
		'CELERY' : ['FOOD', 'VEGETABLES'],
		'CORN' : ['FOOD', 'VEGETABLES'],
		'CUCUMBERS' : ['FOOD', 'VEGETABLES'],
		'LETTUCE' : ['FOOD', 'VEGETABLES'],
		'GREENS' : ['FOOD', 'VEGETABLES'],
		'MUSHROOMS' : ['FOOD', 'VEGETABLES'],
		'ONIONS' : ['FOOD', 'VEGETABLES'],
		'PEPPERS' : ['FOOD', 'VEGETABLES'],
		'POTATOES' : ['FOOD', 'VEGETABLES'],
		'SPINACH' : ['FOOD', 'VEGETABLES'],
		'SQUASH' : ['FOOD', 'VEGETABLES'],
		'ZUCCHINI' : ['FOOD', 'VEGETABLES'],
		'TOMATOES' : ['FOOD', 'VEGETABLES'],
		'APPLES' : ['FOOD', 'FRUITS'],
		'AVOCADOS' : ['FOOD', 'FRUITS'],
		'BERRIES' : ['FOOD', 'FRUITS'],
		'CHERRIES' : ['FOOD', 'FRUITS'],
		'GRAPEFRUIT' : ['FOOD', 'FRUITS'],
		'GRAPES' : ['FOOD', 'FRUITS'],
		'KIWIS' : ['FOOD', 'FRUITS'],
		'LEMON' : ['FOOD', 'FRUITS'],
		'LIMES' : ['FOOD', 'FRUITS'],
		'MELON' : ['FOOD', 'FRUITS'],
		'NECTARINES' : ['FOOD', 'FRUITS'],
		'ORANGES' : ['FOOD', 'FRUITS'],
		'PEACHES' : ['FOOD', 'FRUITS'],
		'PEARS' : ['FOOD', 'FRUITS'],
		'PLUMS' : ['FOOD', 'FRUITS'],
		'BUTTER' : ['FOOD', 'DAIRY'],
		'MARGARINE' : ['FOOD', 'DAIRY'],
		'COTTAGE CHEESE' : ['FOOD', 'DAIRY'],
		'MILK' : ['FOOD', 'DAIRY'],
		'SOUR CREAM' : ['FOOD', 'DAIRY'],
		'WHIPPED CREAM' : ['FOOD', 'DAIRY'],
		'YOGURT' : ['FOOD', 'DAIRY'],
		'BACON' : ['FOOD', 'MEATS'],
		'SAUSAGE' : ['FOOD', 'MEATS'],
		'BEEF' : ['FOOD', 'MEATS'],
		'CHICKEN' : ['FOOD', 'MEATS'],
		'GROUND BEEF' : ['FOOD', 'MEATS'],
		'TURKEY' : ['FOOD', 'MEATS'],
		'HAM' : ['FOOD', 'MEATS'],
		'PORK' : ['FOOD', 'MEATS'],
		'HOT DOGS' : ['FOOD', 'MEATS'],
		'LUNCHMEAT' : ['FOOD', 'MEATS'],
		'TURKEY' : ['FOOD', 'MEATS'],
		'ANTIPERSPIRANT ' : ['PERSONAL CARE'],
		'DEODORANT' : ['PERSONAL CARE'],
		'BATH SOAP' : ['PERSONAL CARE'],
		'HAND SOAP' : ['PERSONAL CARE'],
		'CONDOMS' : ['PERSONAL CARE'],
		'COSMETICS' : ['PERSONAL CARE'],
		'COTTON SWABS ' : ['PERSONAL CARE'],
		'BALLS' : ['PERSONAL CARE'],
		'FACIAL CLEANSER' : ['PERSONAL CARE'],
		'FACIAL TISSUE' : ['PERSONAL CARE'],
		'FEMININE PRODUCTS' : ['PERSONAL CARE'],
		'FLOSS' : ['PERSONAL CARE'],
		'HAIR GEL ' : ['PERSONAL CARE'],
		'SPRAY' : ['PERSONAL CARE'],
		'LIP BALM' : ['PERSONAL CARE'],
		'MOISTURIZING LOTION' : ['PERSONAL CARE'],
		'MOUTHWASH' : ['PERSONAL CARE'],
		'RAZORS' : ['PERSONAL CARE'],
		'SHAVING CREAM' : ['PERSONAL CARE'],
		'SHAMPOO' : ['PERSONAL CARE'],
		'CONDITIONER' : ['PERSONAL CARE'],
		'SUNBLOCK' : ['PERSONAL CARE'],
		'TOILET PAPER' : ['PERSONAL CARE'],
		'TOOTHPASTE' : ['PERSONAL CARE'],
		'VITAMINS' : ['PERSONAL CARE'],
		'SUPPLEMENTS' : ['PERSONAL CARE']
	}

	@staticmethod
	def getItemTags(stringToTag):
		words = stringToTag.split()
		tagSet = Set()
		for word in words:
			if word.upper() in Tagger.ITEM_TAGS_MAP:
				tags = Tagger.ITEM_TAGS_MAP[word.upper()]
				for x in tags:
					tagSet.add(x)
		return list(tagSet)


def get_item_tags(parsed_rows):
	tagged_rows = list()
	for row in parsed_rows:
		tags = Tagger.getItemTags(row)
		if tags == []:
			continue
		tags.insert(0, row)
		# print(tags)
		tagged_rows.append(tags)
	return tagged_rows
# Example
# print(Tagger.getItemTags('Bananas and Bacon'))
# returns ['FOOD', 'MEATS', 'FRUITS']