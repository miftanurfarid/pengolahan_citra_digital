"""
script ini akan melakukan blending 2 citra menjadi satu secara interpolasi dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image

im1 = Image.open("../dataset/mountain.jpg")
im2 = Image.open("../dataset/rose.png")

print(im1.width, im1.height, im1.mode)
print(im2.width, im2.height, im2.mode)

im1 = im1.convert('RGB')
im2 = im2.resize((im1.width, im1.height), Image.BILINEAR)
im = Image.blend(im1, im2, alpha=0.5)
im.show()
