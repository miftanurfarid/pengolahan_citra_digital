from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
from scipy import signal
import scipy.fftpack as fp
from matplotlib import pylab

im = rgb2gray(imread('./dataset/rose.jpg'))
gauss_kernel = np.outer(signal.windows.gaussian(im.shape[0], 1),
                        signal.windows.gaussian(im.shape[1], 1))
freq = fp.fft2(im)
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))
pylab.imshow((20 * np.log10(0.01 +
                            fp.fftshift(freq_kernel))).real.astype(int),
             cmap='coolwarm')  # 0.01 is added to keep the argument to log function always positive
pylab.colorbar()
pylab.title("Gaussian kernel spectrum")
pylab.show()
