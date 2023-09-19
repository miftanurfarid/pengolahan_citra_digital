"""
script ini akan melakukan converting mode
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread
from skimage import color
import matplotlib.pylab as plt

im = imread("../dataset/ishihara.png")
im_g = color.rgb2gray(im)
plt.subplot(121), plt.imshow(im, cmap='gray'), plt.axis('off'), plt.title('Citra RGB')
plt.subplot(122), plt.imshow(im_g, cmap='gray'), plt.axis('off'), plt.title('Citra GRAY')
plt.show()
