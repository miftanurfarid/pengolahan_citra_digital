"""
script ini akan menampilkan perbedaan dari 2 citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
from PIL.ImageChops import difference, subtract, screen
import matplotlib.pylab as plt

im1 = Image.open("../dataset/th1.jpeg")
im2 = Image.open("../dataset/th2.jpeg")

im3 = difference(im1, im2)
im4 = subtract(im1, im2)
im5 = screen(im1, im2)

plt.subplot(231)
plt.imshow(im1)
plt.title('citra 1')
plt.subplot(232)
plt.imshow(im2)
plt.title('citra 2')
plt.subplot(234)
plt.imshow(im3)
plt.title('citra hasil difference')
plt.subplot(235)
plt.imshow(im4)
plt.title('citra hasil subtract')
plt.subplot(236)
plt.imshow(im5)
plt.title('citra hasil screen')
plt.show()
