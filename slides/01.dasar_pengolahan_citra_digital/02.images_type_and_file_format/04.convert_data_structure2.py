"""
script ini akan melakukan converting dari numpy ndarray menjadi PIL Image object
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""
from skimage.io import imread
from PIL import Image

im = imread("../dataset/rose.png")  # membaca citra menjadi Image object
print(im.shape, im.dtype, type(im))

im = Image.fromarray(im)
print(im.width, im.height, im.mode, im.format, type(im))

im.show()
