from matplotlib import pylab
import numpy as np
from scipy import ndimage
from skimage.io import imread
import scipy.fftpack as fp


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return 20 * np.log10(np.where(sd == 0, 0, m / sd))


fig, (axes1, axes2) = pylab.subplots(1, 2, figsize=(10, 5))
pylab.gray()  # show the result in grayscale
im = np.mean(imread('../dataset/building.jpg'), axis=2)
freq = fp.fft2(im)
freq_gaussian = ndimage.fourier_gaussian(freq, sigma=4)
im1 = np.fft.ifft2(freq_gaussian)
print(f'SNR sebelum LPF = {signaltonoise(im, axis=None)}')
print(f'SNR setelah LPF = {signaltonoise(im1.real, axis=None)}')
axes1.imshow(im)
axes1.set_title('Citra asli')
axes2.imshow(im1.real)  # the imaginary part is an artifact
axes2.set_title('Citra hasil LPF')

pylab.figure(figsize=(10, 5))
pylab.subplot(121)
pylab.imshow((20 * np.log10(0.1 + np.fft.fftshift(freq))).real.astype(int))
pylab.title('Spectrum citra sebelum LPF')
pylab.subplot(122)
pylab.imshow((20 * np.log10(0.1 + np.fft.fftshift(freq_gaussian))).real.astype(int))
pylab.title('Spectrum citra setelah LPF')
pylab.show()
