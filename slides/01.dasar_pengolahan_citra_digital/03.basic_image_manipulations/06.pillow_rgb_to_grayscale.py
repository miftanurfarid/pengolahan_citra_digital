"""
script ini akan melakukan gray-level transformations terhadap citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image, ImageShow
import numpy as np

im = Image.open('../dataset/rose.png')
im.show(title='Citra asli')

im_g = im.convert('L')
im_g.show(title='Citra grayscale')

img_log_trans = im_g.point(lambda x: 255 * np.log(1 + x / 255))
img_log_trans.show(title='Citra grayscale dengan log transformation')

gamma = 0.6
img_pow_law = im_g.point(lambda x: 255 * (x / 255) ** gamma)
img_pow_law.show(title='Citra grayscale dengan power-law transformation')

im.transform((int(1.4*im.width), im.height), Image.AFFINE,
data=(1,-0.5,0,0,1,0)).show()