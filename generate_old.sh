#!/bin/bash
mkdir most_2000/valid_old
for filename in most_2000/valid/*.JPEG; do
	echo $filename
	python colorize.py --caffemodel models/init_v2.caffemodel -img_in $filename -img_out ${filename/valid/valid_old}
done

for filename in most_2000/valid_old/*.JPEG; do
	fnew=${filename/valid_old/valid}
	cp $filename ${fnew/.JPEG/_old.JPEG}
done