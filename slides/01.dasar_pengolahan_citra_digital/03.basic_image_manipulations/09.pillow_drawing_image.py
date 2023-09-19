"""
script ini akan menggambar garis dan bentuk geometrik lainnya pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image, ImageDraw
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
draw = ImageDraw.Draw(im)
draw.ellipse((125, 125, 200, 250), fill=(255, 255, 255, 128))
del draw
plt.imshow(im)
plt.show()
