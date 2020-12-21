import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np

colors = []
# Image.mode('rgba')
for i in range(14400):
	file = Image.open("frame" + str(i) + ".jpg")
#	file.mode('rgba')
	Image.mode = "rgba"
	r = 0
	g = 0
	b = 0
	#a, b, c, alpha = file.split()
	#for j in range(160):
	#	for k in range(90):
	#		# pixel = file.getpixel((j, k))
	#		# a, b, c, alpha = pixel
	for pix in file.getdata():
		a, b, c, alpha = pix
		r += a * alpha
		g += b * alpha
		b += c * alpha
	color = (r/14400, g/14400, b/14400)
	colors.append(color)
file = open("out", "w")
file.write(str(colors))

