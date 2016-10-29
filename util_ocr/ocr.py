#ocr.py

# import sys
# print sys.path

# from PIL import Image
# from pytesser import *

# im = Image.open('bill_walmart.jpg')
# text = image_to_string(im)
# print text

import re


exlude_list = ['ITEM', 'SOLD', 'TOTAL', 'MONEY', 'SUBTOTAL']
def is_num(s):
	try:
		float(s)
		return True
	except ValueError:
		# if s.upper in exlude_list:
			# return True
		return False

def is_excluded2(s):
	if s.upper() in exlude_list:
		return True
	else:
		return False

tex = "^ UTIL LIGHTER sold 00933\400054 0.08 X"
# lst = 
print tex.split(' ')

lst = re.findall(r"[\w']+", tex)

# print re.split('; |, |\*|^\n', tex)
print lst

lst2 = [x for x in lst if not is_excluded2(x)]
print lst2



print 'sold'.upper() in exlude_list


def is_barcode(s):
	chars = list(s)
	numcount = sum(1 for x in chars if is_num(x))
	if numcount > 0.5 * len(s):
		return True
	else:
		return False

print is_barcode('003QOOQ00673')
