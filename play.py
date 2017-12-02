import os, datetime
import numpy as np
import sys
import string
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import CountVectorizer
from torch.autograd import Variable
from PIL import Image
import glob
import matplotlib.image as mpimg
import numpy as np

image_gt_list = []
count = 1
for filename in glob.glob('training_data/colorization.eecs.berkeley.edu/imgs/gt_imgs_0/*.png'): #assuming png
    im=mpimg.imread(filename)
    image_gt_list.append(im)
    if count == 8000:
    	print(filename)
    count = count + 1

print("Uploaded all ground truth images")

image_cr_list = []
for filename in glob.glob('training_data/colorization.eecs.berkeley.edu/imgs/classrebal_turk_imgs_438000/*.png'): #assuming png
    im=mpimg.imread(filename)
    image_cr_list.append(im)

print("Uploaded all created images")

training_pos = image_gt_list[:int(len(image_gt_list)*0.8)]
training_neg = image_cr_list[:int(len(image_gt_list)*0.8)]

test_pos = image_gt_list[int(len(image_gt_list)*0.8):]
test_neg = image_cr_list[int(len(image_gt_list)*0.8):]

print(len(training_pos), len(training_neg), len(test_pos), len(test_neg))