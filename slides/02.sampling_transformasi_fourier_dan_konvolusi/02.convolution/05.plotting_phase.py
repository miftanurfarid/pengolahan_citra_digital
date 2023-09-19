import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from matplotlib import pylab
import scipy.fftpack as fp

im1 = rgb2gray(imread('../dataset/rose.jpg'))
pylab.figure()
freq1 = fp.fft2(im1)
im1_ = fp.ifft2(freq1).real
pylab.subplot(2, 2, 1), pylab.imshow(im1, cmap='gray'), pylab.title('Original Image')
pylab.subplot(2, 2, 2), pylab.imshow(20 * np.log10(0.01 + np.abs(fp.fftshift(freq1))), cmap='gray')
pylab.title('FFT Spectrum Magnitude')
pylab.subplot(2, 2, 3), pylab.imshow(np.angle(fp.fftshift(freq1)), cmap='gray')
pylab.title('FFT Phase')
pylab.subplot(2, 2, 4), pylab.imshow(np.clip(im1_, 0, 255), cmap='gray')
pylab.title('Reconstructed Image')
pylab.show()
