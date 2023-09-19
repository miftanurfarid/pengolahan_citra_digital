"""
script ini akan melakukan converting dari PIL Image object menjadi numpy ndarray
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""
from PIL import Image
import numpy as np
from skimage.io import imshow, show

im = Image.open("../dataset/rose.png")  # membaca citra menjadi Image object
print(im.width, im.height, im.mode, im.format, type(im))

im = np.array(im)  # membuat numpy ndarray dari Image object
print(im.shape, im.dtype, type(im))

imshow(im)
show()
