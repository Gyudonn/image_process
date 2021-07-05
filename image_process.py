from PIL import Image
import os

for file in os.listdir('orig'):
	if file.endswith('.jpg'):
		#http://www.sharejs.com
		image_file = Image.open(os.path.join('orig', file))
		image_file = image_file.convert('1')
		image_file.save(os.path.join('result', file[:-4] + '_grey.png'))