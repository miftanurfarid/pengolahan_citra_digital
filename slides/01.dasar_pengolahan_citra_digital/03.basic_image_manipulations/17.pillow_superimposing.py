"""
script ini akan melakukan superimposing 2 citra menjadi satu dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
from PIL.ImageChops import multiply

im1 = Image.open("../dataset/rose.png")
im2 = Image.open("../dataset/mountain.jpg").resize((im1.width, im1.height))
im = multiply(im1, im2)
im.show()
