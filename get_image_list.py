from os import listdir
from os.path import isfile, join

imageID2label = {}
imndesc2id = {}
IL2012toname = {}

with open("image_net_labels.txt",'r') as file:
	for item in file.read().splitlines():
		ID, desc = item[1:-1].split(": ")
		desc = desc[1:-1]
		imndesc2id[desc] = int(ID)

with open("ImageNet_data/2012ID_to_words.txt",'r') as file:
	for item in file.read().splitlines():
		ID, wnid, name = item.split('\t')
		IL2012toname[int(ID)] = name

with open("ImageNet_data/ILSVRC2012_devkit_t12/data/ILSVRC2012_validation_ground_truth.txt",'r') as file:
	lines = file.read().splitlines()
	for i in range(50000):
		ID = lines[i]
		desc = IL2012toname[int(ID)]
		new_id = imndesc2id[desc]
		imageID2label[i+1] = new_id

for filetype in ["train", "valid"]:
	mypath = "most_2000/" + filetype
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	print(onlyfiles)
	with open("most_2000_%s.txt" % filetype, "a") as file:
		for filename in onlyfiles:
			file.write(filename+(" %d\n" % imageID2label[int(filename[:5])]))
			