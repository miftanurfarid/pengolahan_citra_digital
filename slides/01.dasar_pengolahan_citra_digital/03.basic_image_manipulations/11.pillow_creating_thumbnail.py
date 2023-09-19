"""
script ini akan membuat thumbnail pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
im_thumbnail = im.copy()
im_thumbnail.thumbnail((250,250))
im.paste(im_thumbnail, (10,10))
im.save("../dataset/rose_thumb.png")
plt.imshow(im)
plt.show()
