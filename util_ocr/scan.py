# import the necessary packages

''' need to install 
scikit-image
imutils
pytesser
tesseract - not a python lib
opencv
numpy
'''

from pyimagesearch.transform import four_point_transform
# from pyimagesearch 
import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import argparse
import cv2
from PIL import Image
from pytesser import *
import re

exclude_list = ['ITEM', 'SOLD', 'TOTAL', 'MONEY', 'SUBTOTAL', 'TAX', 'CHANGE'] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ^#")

def is_num(s):
	try:
		float(s)
		return True
	except ValueError:
		# if s.upper in exclude_list:
			# return True
		return False

def is_excluded(s):
	if s.upper() in exclude_list:
		return True
	else:
		return False

# assume barcode if numbers are more than half num chars in string
def is_barcode(s):
	chars = list(s)
	numcount = sum(1 for x in chars if is_num(x))
	if numcount >= 0.4 * len(s):
		return True
	else:
		return False

def ocr_image(imgpath):
	# construct the argument parser and parse the arguments
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--image", required = True,
	# 	help = "Path to the image to be scanned")
	# args = vars(ap.parse_args())

	# load the image and compute the ratio of the old height
	# to the new height, clone it, and resize it
	# image = cv2.imread(args["image"])
	image = cv2.imread(imgpath)
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)
	 
	# convert the image to grayscale, blur it, and find edges
	# in the image
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 75, 200)
	 
	# show the original image and the edge detected image
	print "STEP 1: Edge Detection"
	# cv2.imshow("Image", image)
	# cv2.imshow("Edged", edged)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# find the contours in the edged image, keeping only the
	# largest ones, and initialize the screen contour
	(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
	 
	# loop over the contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	 
		# if our approximated contour has four points, then we
		# can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break
		else:
			print "found only these point:", approx
	 
	# show the contour (outline) of the piece of paper
	print "STEP 2: Find contours of paper"
	# cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
	# cv2.imshow("Outline", image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# apply the four point transform to obtain a top-down
	# view of the original image
	warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
	 
	# convert the warped image to grayscale, then threshold it
	# to give it that 'black and white' paper effect
	warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	warped = threshold_adaptive(warped, 251, offset = 10)
	warped = warped.astype("uint8") * 255
	 
	# show the original and scanned images
	print "STEP 3: Apply perspective transform"
	# cv2.imshow("Original", imutils.resize(orig, height = 650))
	# cv2.imshow("Scanned", imutils.resize(warped, height = 650))
	# cv2.waitKey(0)
	outname = 'warp.png'
	cv2.imwrite(outname, warped)


	im = Image.open(outname)
	text = image_to_string(im)
	itemlist = text.split('\n')
	token_list = [re.findall(r"[\w']+", x) for x in itemlist]

	clean_list = list()
	for row in token_list:
		temp = [x for x in row if not is_num(x) and not is_excluded(x) and not is_barcode(x)]
		clean_list.append(temp)
		# temp = [y for y in x if not is_num(x)]

	retlist = list()
	for x in clean_list:
		if x == []:
			continue
		word =  ' '.join(x)
		retlist.append(word)

	return retlist	


	# lst = re.findall(r"[\w']+", tex)

