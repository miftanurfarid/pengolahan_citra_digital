from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
import scipy.fftpack as fp
from scipy import signal
from matplotlib import pylab

im = 255 * rgb2gray(imread('../dataset/rose.jpg'))
gauss_kernel = np.outer(signal.windows.gaussian(im.shape[0], 3),
                        signal.windows.gaussian(im.shape[1], 3))
freq = fp.fft2(im)  # F(u,v)
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))  # H(u,v)
convolved = freq * freq_kernel  # G(u,v) = H(u,v) x F(u,v)
im_blur = fp.ifft2(convolved).real
im_blur = 255 * im_blur / np.max(im_blur)  # normalisasi

epsilon = 10 ** -6  # akan digunakan untuk menghilangkan division by zero
freq_blur = fp.fft2(im_blur)  # G(u,v)
freq_kernel = 1 / (epsilon + freq_kernel)  # 1 / H(u,v)
convolved2 = freq_blur * freq_kernel  # F(u,v) = G(u,v) / H(u,v)
im_restored = fp.ifft2(convolved2).real
im_restored = 255 * im_restored / np.max(im_restored)
print(np.max(im), np.max(im_restored))
pylab.figure(figsize=(9, 6))
pylab.gray()
pylab.subplot(221), pylab.imshow(im), pylab.title('Citra asli')
pylab.subplot(222), pylab.imshow(im_blur), pylab.title('Citra blur'),
pylab.subplot(223), pylab.imshow(im_restored), pylab.title('Restoration citra')
pylab.subplot(224), pylab.imshow(im_restored - im), pylab.title('Perbedaan antara citra asli dan restoration citra')
pylab.show()
