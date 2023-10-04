from matplotlib import pylab
import numpy as np
import scipy.fftpack as fp
from scipy import signal
from skimage.io import imread

pylab.figure(figsize=[10,6])
pylab.gray()  # show the filtered result in grayscale
im = np.mean(imread('../dataset/building.jpg'), axis=2)
gauss_kernel = np.outer(signal.windows.gaussian(im.shape[0], 5),
                        signal.windows.gaussian(im.shape[1], 5))
freq = fp.fft2(im)
assert (freq.shape == gauss_kernel.shape)
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))
convolved = freq * freq_kernel  # by the convolution theorem, simply multiply in the frequency domain
im1 = fp.ifft2(convolved).real

pylab.subplot(2, 3, 1)
pylab.imshow(im)
pylab.title('Citra masukan')

pylab.subplot(2, 3, 2)
pylab.imshow(gauss_kernel)
pylab.title('Gaussian Kernel')

pylab.subplot(2, 3, 3)
pylab.imshow(im1)  # the imaginary part is an artifact
pylab.title('Citra luaran')

pylab.subplot(2, 3, 4)
pylab.imshow((20 * np.log10(0.1 + fp.fftshift(freq))).real.astype(int))
pylab.title('Spectrum dari citra masukan')

pylab.subplot(2, 3, 5)
pylab.imshow((20 * np.log10(0.1 + fp.fftshift(freq_kernel))).real.astype(int))
pylab.title('Gaussian Kernel Spectrum')

pylab.subplot(2, 3, 6)
pylab.imshow((20 * np.log10(0.1 + fp.fftshift(convolved))).real.astype(int))
pylab.title('Spectrum dari citra luaran')

pylab.show()
