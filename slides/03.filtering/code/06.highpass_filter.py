import numpy as np
from PIL import Image
from matplotlib import pylab
import scipy.fftpack as fp


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return 20 * np.log10(np.where(sd == 0, 0, m / sd))


im = np.array(Image.open('../dataset/building.jpg').convert('L'))
pylab.figure(figsize=[6, 5])
pylab.subplot(221)
pylab.imshow(im, cmap='gray')
pylab.title('Citra')

freq = fp.fft2(im)
(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)
freq1 = np.copy(freq)
freq2 = fp.fftshift(freq1)
pylab.subplot(222)
pylab.imshow((20 * np.log10(0.1 + freq2)).real.astype(int))
pylab.title('Spectrum citra')

freq2[half_w - 10:half_w + 11,
half_h - 10:half_h + 11] = 0  # membuat semua nilai di 20x20 (low) frequencies menjadi nol
pylab.subplot(223)
pylab.imshow((20 * np.log10(0.1 + freq2)).real.astype(int))
pylab.title('Spectrum citra setelah HPF')

im1 = np.clip(fp.ifft2(fp.ifftshift(freq2)).real, 0, 255)  # clip pixel values after IFFT
print(f'SNR citra sebelum HPF = {signaltonoise(im, axis=None)} dB')
print(f'SNR citra setelah HPF = {signaltonoise(im1, axis=None)} dB')
pylab.subplot(224)
pylab.imshow(im1, cmap='gray')
pylab.title('Citra setelah HPF')
pylab.show()
