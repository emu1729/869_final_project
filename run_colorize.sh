#!/bin/bash
mkdir most_2000/valid_new
for filename in most_2000/valid/*.JPEG; do
	echo $filename
	python colorize.py --caffemodel $1 -img_in $filename -img_out ${filename/valid/valid_new}
done

for filename in most_2000/valid_new/*.JPEG; do
	fnew=${filename/valid_new/valid}
	cp $filename ${fnew/.JPEG/_new.JPEG}
done