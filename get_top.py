import re
import urllib
import os
import random
from shutil import copyfile

random.seed(1)

with open('sorted_gt.txt') as file:
	lines = file.read().splitlines()[0][1:-1]
	image_names = re.split("\(|\)|,|\'| ",lines)
	total = 0
	random.shuffle(image_names)
	for name in image_names:
		if name[:2] == 'gt':
			file_name = name[-10:-5]
			print(total)
			if total < 500:
				copyfile("ImageNet_data/10k/gt/ILSVRC2012_val_000%s.JPEG" % file_name, "most_2000/valid/" + file_name + ".JPEG")
			else:
				copyfile("ImageNet_data/10k/gt/ILSVRC2012_val_000%s.JPEG" % file_name, "most_2000/train/" + file_name + ".JPEG")
			total += 1