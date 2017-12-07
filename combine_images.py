import sys
from PIL import Image

import os

total = 0
for filename in os.listdir("valid_900/"):
	if "old" in filename or "new" in filename or filename[0]=='.':
		continue
	print total, filename
	num = filename[:5]
	images = map(Image.open, ['valid_900/%s.JPEG' % num, 'valid_900/%s_old.JPEG' % num, 'valid_900/%s_new.JPEG'% num])
	images[0] = images[0].convert('LA')
	width, height = images[0].size
	if width > height:
		images = [img.resize((256 * width / height, 256), Image.BILINEAR) for img in images]
	else:
		images = [img.resize((256, 256 * height / width), Image.BILINEAR) for img in images]
	images = [img.crop((0,0,256,256)) for img in images]
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save('valid_grouped_900_grey_cropped/%s.jpg' % num)
	total += 1