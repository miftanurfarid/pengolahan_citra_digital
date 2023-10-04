import numpy as np
from PIL import Image
import scipy.fftpack as fp
from matplotlib import pylab


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return 20 * np.log10(np.where(sd == 0, 0, m / sd))


im = np.array(Image.open('../dataset/building.jpg').convert('L'))
freq = fp.fft2(im)
(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)
freq1 = np.copy(freq)
freq2 = fp.fftshift(freq1)
freq2_low = np.copy(freq2)
freq2_low[half_w - 10:half_w + 11, half_h - 10:half_h + 11] = 0  # block low frequencies
freq2 -= freq2_low  # select only the first 20x20 (low) frequencies, block the high frequencies
im1 = fp.ifft2(fp.ifftshift(freq2)).real
print(f'SNR sebelum LPF = {signaltonoise(im, axis=None)}')
print(f'SNR setelah LPF = {signaltonoise(im1, axis=None)}')
pylab.figure(figsize=[10, 5])
pylab.subplot(121)
pylab.title('Citra sebelum LPF')
pylab.imshow(im, cmap='gray')
pylab.subplot(122)
pylab.title('Citra setelah LPF')
pylab.imshow(im1, cmap='gray')

pylab.figure(figsize=[10, 5])
pylab.subplot(121)
pylab.imshow((20 * np.log10(0.1 + fp.fftshift(freq)).real.astype(int)))
pylab.title('Spectrum citra sebelum LPF')
pylab.subplot(122)
pylab.imshow((20 * np.log10(0.1 + freq2).real.astype(int)))
pylab.title('Spectrum citra setelah LPF')
pylab.show()
