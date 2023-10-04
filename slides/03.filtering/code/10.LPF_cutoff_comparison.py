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
snrs_lp = []
ubs = list(range(1, 25, 2))
pylab.figure(figsize=(10, 6))

idx = 1
for u in ubs:
    freq1 = np.copy(freq)
    freq2 = fp.fftshift(freq1)
    freq2_low = np.copy(freq2)
    freq2_low[half_w - u:half_w + u + 1, half_h - u:half_h + u + 1] = 0
    freq2 -= freq2_low  # select only the first 20x20 (low) frequencies
    im1 = fp.ifft2(fp.ifftshift(freq2)).real
    snrs_lp.append(signaltonoise(im1, axis=None))
    pylab.subplot(3, 4, idx), pylab.imshow(im1, cmap='gray'), pylab.axis('off')
    pylab.title('F = ' + str(u), size=10)
    idx += 1
pylab.subplots_adjust(wspace=0.1, hspace=0)

snr = signaltonoise(im, axis=None)
pylab.figure(figsize=[8, 6])
pylab.plot(ubs, snrs_lp, 'b.-')
pylab.plot(range(25), [snr] * 25, 'r-')
pylab.legend(['SNR citra hasil LPF', 'SNR citra asli'])
pylab.xlabel('Cutoff Freqeuncy for LPF')
pylab.ylabel('SNR')
pylab.grid()
pylab.show()
