from __future__ import print_function
from scan import ocr_image
from ItemTagger import get_item_tags


filepath = 'w1.png'

parsed_text = ocr_image(filepath)

# print(parsed_text)
# parsed_text = ['mar', 'Save muney Lmve better', 'NEIGHBORHOOD MARKET', 'ale zsss', 'MANAGER MARY HALL', "B' TE TR", 'FVLBLSKIMMLK', 'FVLBLSKI LK', 'SK LITE TUNA bananas', 'SUBTQTAL', 'Et LITE TUNA', "SK LITE TUNA '", 'SK LIT TUNA', 'SUBTQTAL', 'HDACHE CAPS', 'EQ VITAMIN5', 'SK TUNA', 'SK LITE TUNA', 'SUETQTAL', 'EABYBEL LITE', 'BABY CARROTS', 'BI LCKYCI RMS', 'JIF TO GO PB', "BAEDIICHES E'", 'BANANAS', 'lb lb', 'BUBTQTAL', 'BE PEPPER', 'CASH TEND', 'DUE', 'ITEMS', 'TC', 'now Prices You can Trust nvexy nay', 'ca as is']


print(get_item_tags(parsed_text))

# for x in parsed_text:
# 	tags = Tagger.getItemTags(x)
# 	if tags == []:
# 		continue
# 	tags.insert(0, x)
# 	print(tags)

