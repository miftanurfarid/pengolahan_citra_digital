"""
script ini akan melakukan perubahan pixel value pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import numpy as np
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
im1 = im.copy()
n = 5000
x, y = np.random.randint(0, im.width, n), np.random.randint(0, im.height, n)
for (x, y) in zip(x, y):
    im1.putpixel((x, y), ((0, 0, 0) if np.random.rand() < 0.5 else (255, 255, 255)))  # salt-and-pepper noise
plt.figure(figsize=(16, 9))
plt.subplot(121)
plt.imshow(im)
plt.title('Citra asli')
plt.subplot(122)
plt.imshow(im1)
plt.title('Citra hasil penambahan salt-and-pepper noise')
plt.show()
