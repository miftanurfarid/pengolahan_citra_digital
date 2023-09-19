from matplotlib import pylab
import scipy.fftpack as fp
import numpy as np
from skimage.color import rgb2gray
from skimage.io import imread

im1 = rgb2gray(imread('../dataset/rose.png'))
freq1 = fp.fft2(im1)

im2 = rgb2gray(imread('../dataset/rose_thumb.png'))
freq2 = fp.fft2(im2)

pylab.figure(figsize=(20, 15))
im1_ = fp.ifft2(np.vectorize(complex)(freq1.real, freq2.imag)).real
im2_ = fp.ifft2(np.vectorize(complex)(freq2.real, freq1.imag)).real
pylab.subplot(211), pylab.imshow(np.clip(im1_, 0, 255), cmap='gray')
pylab.title('Reconstructed Image (Re(F1) + Im(F2))', size=20)
pylab.subplot(212), pylab.imshow(np.clip(im2_, 0, 255), cmap='gray')
pylab.title('Reconstructed Image (Re(F2) + Im(F1))', size=20)
pylab.show()
