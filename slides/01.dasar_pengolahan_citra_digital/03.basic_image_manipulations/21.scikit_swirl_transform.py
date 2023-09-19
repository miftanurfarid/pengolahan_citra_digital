"""
script ini akan melakukan transformasi geometrik terhadap citra dengan memanfaatkan library scikit-image.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread
from skimage.transform import swirl
import matplotlib.pylab as plt

im = imread("../dataset/rose.png")
swirled = swirl(im, rotation=0, strength=30, radius=400)
plt.imshow(swirled)
plt.axis('off')
plt.show()
