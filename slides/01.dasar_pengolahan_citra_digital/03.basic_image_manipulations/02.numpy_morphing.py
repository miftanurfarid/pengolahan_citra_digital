"""
script ini akan melakukan morphing terhadap 2 citra dengan menggunakan library numpy
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pylab as plt

im1 = mpimg.imread("../dataset/test1.jpg") / 255
im2 = mpimg.imread("../dataset/test2.jpg") / 255

i = 1
plt.figure(figsize=(10, 8))
for alpha in np.linspace(0, 1, 20):
    plt.subplot(4, 5, i)
    plt.imshow((1 - alpha) * im1 + alpha * im2)
    plt.axis('off')
    i += 1
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()
