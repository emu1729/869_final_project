import re
import urllib
import os
import random

with open('most_2000_gt_images.txt') as file:
	lines = file.read().splitlines()[0][1:-1]
	image_names = re.split("\(|\)|,|\'| ",lines)
	total = 0
	random.shuffle(image_names)
	total = 0
	for name in image_names:
		if name[:2] == 'gt':
			file_name = name[3:]
			if total < 500:
				urllib.urlretrieve("http://colorization.eecs.berkeley.edu/imgs/gt_imgs_0/" + file_name, filename="most_2000/valid/" + file_name)
			else:
				urllib.urlretrieve("http://colorization.eecs.berkeley.edu/imgs/gt_imgs_0/" + file_name, filename="most_2000/train/" + file_name)
			total += 1