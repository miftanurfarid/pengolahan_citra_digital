"""
script ini akan melakukan slicing terhadap citra dengan menggunakan library numpy
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pylab as plt

rose = mpimg.imread("../dataset/rose.jpg")
print(rose.shape, rose.dtype, type(rose))
lx, ly, _ = rose.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
rose_copy = rose.copy()
rose_copy[mask,:] = 0 # masks
plt.figure()
plt.imshow(rose_copy), plt.axis('off'), plt.show()
