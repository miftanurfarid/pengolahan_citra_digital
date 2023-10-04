import numpy as np
from skimage.io import imread
from scipy import signal
from matplotlib import pylab
import scipy.fftpack as fp

im = np.mean(imread('../dataset/building.jpg'), axis=2)
# 2D Gaussian kernel of size 11x11 with σ = 3
gauss_kernel = np.outer(signal.windows.gaussian(11, 3), signal.windows.gaussian(11, 3))
im_blurred = signal.fftconvolve(im, gauss_kernel, mode='same')
fig, (ax_original, ax_kernel, ax_blurred) = pylab.subplots(1, 3, figsize=(8, 6))
ax_original.imshow(im, cmap='gray')
ax_original.set_title('Citra asli')
ax_kernel.imshow(gauss_kernel)
ax_kernel.set_title('Gaussian kernel')
ax_blurred.imshow(im_blurred, cmap='gray')
ax_blurred.set_title('Blurred')

F1 = fp.fft2(im.astype(float))
F2 = fp.fftshift(F1)
pylab.figure(figsize=(8, 6))
pylab.subplot(1, 2, 1), pylab.imshow((20 * np.log10(0.1 + F2)).real.astype(int), cmap='gray')
pylab.title('Spectrum citra asli')
F1 = fp.fft2(im_blurred.astype(float))
F2 = fp.fftshift(F1)
pylab.subplot(1, 2, 2), pylab.imshow((20 * np.log10(0.1 + F2)).real.astype(int), cmap='gray')
pylab.title('Spectrum citra blurred')
pylab.show()
