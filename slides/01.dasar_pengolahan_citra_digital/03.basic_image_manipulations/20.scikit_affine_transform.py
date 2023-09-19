"""
script ini akan melakukan transformasi geometrik terhadap citra dengan memanfaatkan library scikit-image.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread
from skimage.transform import SimilarityTransform, warp
import numpy as np
import matplotlib.pyplot as plt

im = imread("../dataset/rose.png")
tform = SimilarityTransform(scale=0.9, rotation=np.pi / 4, translation=(im.shape[0] / 2, -100))
warped = warp(im, tform)

plt.imshow(warped), plt.axis('off'), plt.show()
