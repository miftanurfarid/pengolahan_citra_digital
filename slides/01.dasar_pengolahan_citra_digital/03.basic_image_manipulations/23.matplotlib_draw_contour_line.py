"""
script ini akan menggambar garis kontur terhadap citra dengan memanfaatkan library matplotlib.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread
from skimage import color
import matplotlib.pylab as plt
import numpy as np

im = color.rgb2gray(imread("../dataset/rose.jpg"))
plt.figure(figsize=(16, 3))
plt.subplot(131), plt.imshow(im, cmap='gray'), plt.title('Original Image', size=20)
plt.subplot(132), plt.contour(np.flipud(im), colors='k', levels=np.logspace(-15, 15, 100)), plt.title(
    'Image Contour Lines', size=20)
plt.subplot(133), plt.title('Image Filled Contour', size=20),
plt.contourf(np.flipud(im), cmap='inferno')
plt.show()
