import numpy as np
from matplotlib import pylab
from scipy import signal
from skimage.util import img_as_float

im = img_as_float(pylab.imread('../dataset/building.jpg'))

x = np.linspace(-10, 10, 15)

kernel_1d = np.exp(-0.005*x**2)
kernel_1d /= np.trapz(kernel_1d) # normalize the sum to 1
gauss_kernel1 = kernel_1d[:, np.newaxis] * kernel_1d[np.newaxis, :]

kernel_1d = np.exp(-5*x**2)
kernel_1d /= np.trapz(kernel_1d) # normalize the sum to 1
gauss_kernel2 = kernel_1d[:, np.newaxis] * kernel_1d[np.newaxis, :]

DoGKernel = gauss_kernel1[:, :, np.newaxis] - gauss_kernel2[:, :, np.newaxis]

im1 = signal.fftconvolve(im, DoGKernel, mode='same')

pylab.figure(figsize=[10,6])
pylab.subplot(121)
pylab.imshow(im)
pylab.title('Citra asli')
pylab.subplot(122)
pylab.imshow(np.clip(im1, 0, 1))
pylab.title('Citra hasil BPF DoG')
pylab.show()
