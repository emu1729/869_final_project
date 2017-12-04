from os import listdir
from os.path import isfile, join

for filetype in ["train", "valid"]:
	mypath = "most_2000/" + filetype
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	print onlyfiles
	with open("most_2000_%s.txt" % filetype, "a") as file:
		for filename in onlyfiles:
			file.write(filename+" 0\n")