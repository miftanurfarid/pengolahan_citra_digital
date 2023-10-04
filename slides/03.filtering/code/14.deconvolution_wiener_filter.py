from matplotlib import pylab
from skimage import restoration
from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
from scipy import signal


im = rgb2gray(imread('../dataset/rose.jpg'))
n = 7
psf = np.ones((n, n)) / n**2
im1 = signal.convolve2d(im, psf, 'same')
im1 += 0.1 * im1.std() * np.random.standard_normal(im.shape)
im2, _ = restoration.unsupervised_wiener(im1, psf)

fig, axes = pylab.subplots(nrows=1, ncols=3, figsize=(10, 4), sharex=True, sharey=True)
pylab.gray()
axes[0].imshow(im), axes[0].axis('off'), axes[0].set_title('Citra asli', size=10)
axes[1].imshow(im1), axes[1].axis('off'), axes[1].set_title('Citra noisy & blurry', size=10)
axes[2].imshow(im2), axes[2].axis('off'), axes[2].set_title('Self tuned restoration', size=10)

fig.tight_layout()
pylab.show()
