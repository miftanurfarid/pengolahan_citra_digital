"""
script ini akan melakukan negating terhadap citra dengan menggunakan library pillow
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
im_t = im.point(lambda x: 255 - x)

plt.subplot(121)
plt.imshow(im), plt.title('original')
plt.subplot(122)
plt.imshow(im_t), plt.title('negate')
plt.show()
