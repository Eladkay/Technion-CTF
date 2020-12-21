import ast
import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np
file = open("out", "r")
list = ast.literal_eval(file.read())
pixels = []
for pixel in list:
	x, y, z = pixel
	pixels.append((int(x), int(y), int(z)))
img_ex = Image.open("frame0.jpg")
new_img = Image.new(img_ex.mode, img_ex.size)
new_img.putdata(pixels)
new_img.save("out.jpg")
