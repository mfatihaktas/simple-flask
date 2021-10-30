## Refs:
## - https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays

import sys, random, os
import numpy as np
from PIL import Image
from config import *

# TODO: Change this with a proper log file as in: https://github.com/mfatihaktas/edge-flow-control/blob/master/debug_utils.py
## Note: Python's logging package collides with the flask logger
def print_(s):
	print(s, file=sys.stdout)

def narray_from_img(filename):
	try:
		img = Image.open(full_path(filename)) # .convert('L') # converts to grayscale
	except FileNotFoundError:
		print_("narray_from_img: file not found, filename= {}".format(filename))
		return None

	return np.asarray(img)

def resize_img_in_place(filename, width: int, height: int):
	print_("resize_img_in_place: started;")
	path = full_path(filename)
	try:
		img = Image.open(path)
	except FileNotFoundError:
		print_("resize_img_in_place: file not found, filename= {}".format(filename))
		return None

	img_ = img.resize((width, height))
	img_.save(path)
	print_("resize_img_in_place: done.")

def get_random_slice_from_narray(narray, width: int, height: int):
	x_lim = narray.shape[0] - width
	y_lim = narray.shape[1] - height
	if x_lim < 0 or y_lim < 0:
		print_("Image is not large enough for the given width or height.")
		return None

	x_pos = random.randrange(x_lim)
	y_pos = random.randrange(y_lim)
	print_("x_pos= {}, y_pos= {}".format(x_pos, y_pos))
	return (x_pos, y_pos), narray[x_pos:x_pos+width, y_pos:y_pos+height, :]

def get_random_rect_from_img(filename, width: int=100, height: int=100):
	narray = narray_from_img(filename)
	print_("narray.shape= {}".format(narray.shape))

	return get_random_slice_from_narray(narray, width, height)

def get_two_random_rects_from_img(filename, width: int=100, height: int=100):
	# TODO: Followed the instruction 6 here. However, it would be faster to call narray_from_img once.
	xy_pos1, rect1,  = get_random_rect_from_img(filename, width, height)
	xy_pos2, rect2 = get_random_rect_from_img(filename, width, height)
	return xy_pos1, rect1, xy_pos2, rect2

## TODO: Did not quite understand how to compute a confusion matrix from two image samples.
## For now, will treat each pixel as the value of a single feature collected from a sample --
## whole image is simple an array of sample values in this case. For this, Will normalize the
## pixel values, and will take each as 0 (resp. 1) if the (normalized) value is < (resp. >=) 0.5.
##
## Refs:
## - https://towardsdatascience.com/visual-guide-to-the-confusion-matrix-bb63730c8eba
## - https://en.wikipedia.org/wiki/Confusion_matrix
def get_confusion_matrix_in_dict(truth_narray, test_narray):
	if truth_narray.shape != test_narray.shape:
		print_("Truth and test arrays do not have the same shape.")
		return None

	def get_normed_narray(narray):
		m = np.amax(narray)
		if m == 0:
			return narray
		else:
			narray_ = narray / m

			narray_[narray_ < 0.5] = 0
			narray_[narray_ >= 0.5] = 1
			return narray_

	truth_narray_ = get_normed_narray(truth_narray)
	test_narray_ = get_normed_narray(test_narray)

	def correct_prediction_rate(truth_narray, test_narray, true_val):
		indices = truth_narray == true_val
		eq = truth_narray[indices] == test_narray[indices]
		return np.sum(eq)/np.sum(indices)

	true_positive = correct_prediction_rate(truth_narray_, test_narray_, true_val=1)
	false_negative = 1 - true_positive
	true_negative = correct_prediction_rate(truth_narray_, test_narray_, true_val=0)
	false_positive = 1 - true_negative
	return {'true_positive': true_positive,
					'false_positive': false_positive,
					'true_negative': true_negative,
					'false_negative': false_negative}

def get_perc_overlap_between_two_rects(width, height, xy_pos1, xy_pos2):
	x1, y1 = xy_pos1
	x2, y2 = xy_pos2
	dx = min(x1 + width, x2 + width) - max(x1, x2)
	dy = min(y1 + height, y2 + height) - max(y1, y2)
	if (dx < 0) or (dy < 0):
		return 0
	return dx*dy/(width * height) * 100

def save_narray_as_img(narray, filename):
	print_("save_narray_as_img: started;")
	img = Image.fromarray(narray)
	path = full_path(filename)
	# TODO: img.save seems to set the path to None. Look that up! path_to_return is just a quick hack around it.
	path_to_return = os.path.abspath(path)
	img.save(path)
	print_("save_narray_as_img: done.")
	return path_to_return
