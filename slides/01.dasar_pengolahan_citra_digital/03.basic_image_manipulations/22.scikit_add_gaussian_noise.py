"""
script ini akan menampahkan Gaussian noise terhadap citra dengan memanfaatkan library scikit-image.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread
from skimage.util import img_as_float, random_noise
import matplotlib.pylab as plt

im = img_as_float(imread("../dataset/rose.png"))
plt.figure()
sigmas = [0.1, 0.25, 0.5, 1]
for i in range(4):
    noisy = random_noise(im, var=sigmas[i] ** 2)
    plt.subplot(2, 2, i + 1)
    plt.imshow(noisy)
    plt.axis('off')
    plt.title('Gaussian noise dengan sigma = ' + str(sigmas[i]), size=20)
plt.tight_layout()
plt.show()
