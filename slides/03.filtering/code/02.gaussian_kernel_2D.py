from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
from scipy import signal
import scipy.fftpack as fp
from matplotlib import pylab

im = rgb2gray(imread('../dataset/rose.jpg'))
gauss_kernel = np.outer(signal.windows.gaussian(im.shape[0], 1), signal.windows.gaussian(im.shape[1], 1))
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))
pylab.figure(figsize=[10, 5])
# 0.01 is added to keep the argument to log function always positive
pylab.imshow((20 * np.log10(0.01 + fp.fftshift(freq_kernel))).real.astype(int), cmap='coolwarm')
pylab.title('Gaussian LPF kernel spectrum in 2D')
pylab.colorbar()
pylab.show()
