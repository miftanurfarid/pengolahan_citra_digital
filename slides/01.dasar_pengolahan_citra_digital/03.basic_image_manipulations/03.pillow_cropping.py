"""
script ini akan melakukan cropping terhadap citra dengan menggunakan library pillow
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image

im = Image.open('../dataset/rose.png')
im_c = im.crop((172, 147, 520, 458))  # crop the rectangle given by (left, top, right, bottom) from the image
im_c.show()

