"""
script ini akan menuliskan teks pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 40)
draw.text((10, 5), "Pengolahan Citra Digital 2023", font=font)
del draw
plt.imshow(im)
plt.show()
