from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
from scipy import signal
import scipy.fftpack as fp
from matplotlib import pylab


im = rgb2gray(imread('../dataset/rose.jpg'))
gauss_kernel = np.outer(signal.windows.gaussian(im.shape[0], 1), signal.windows.gaussian(im.shape[1], 1))
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))
X = np.arange(-freq_kernel.shape[1]/2, freq_kernel.shape[1]/2)
Y = np.arange(-freq_kernel.shape[0]/2, freq_kernel.shape[0]/2)
X, Y = np.meshgrid(X, Y)
freq_im = fp.fft2(fp.ifftshift(im))
freq_im_convolved = freq_im * freq_kernel

fig, ax = pylab.subplots(ncols=2, nrows=2, subplot_kw={"projection": "3d"}, figsize=(12, 6))
ax[0][0].plot_surface(X, Y, fp.fftshift(freq_kernel).real.astype(float), cmap='coolwarm')
ax[0][0].set_title('Spectrum 3D dari H(u,v)', size=10)
ax[0][1].plot_surface(X, Y, (20*np.log10(0.01 + fp.fftshift(freq_kernel))).real.astype(float), cmap='coolwarm')
ax[0][1].set_title('Spectrum 3D dari log(H(u,v))', size=10)
ax[1][0].plot_surface(X, Y, (20*np.log10(0.01 + fp.fftshift(freq_im))).real.astype(float), cmap='coolwarm')
ax[1][0].set_title('Spectrum citra sebelum convolution terhadap Gaussian LPF', size=10)
ax[1][1].plot_surface(X, Y, (20*np.log10(0.01 + fp.fftshift(freq_im_convolved))).real.astype(float), cmap='coolwarm')
ax[1][1].set_title('Spectrum citra setelah convolution terhadap Gaussian LPF', size=10)
pylab.show()
