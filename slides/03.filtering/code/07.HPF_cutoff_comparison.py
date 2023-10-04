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
snrs_hp = []
lbs = list(range(1, 25, 2))
pylab.figure(figsize=(10, 6))

idx = 1
for l in lbs:
    freq1 = np.copy(freq)
    freq2 = fp.fftshift(freq1)
    freq2[half_w - l:half_w + l + 1, half_h - l:half_h + l + 1] = 0  # select all but the first lxl (low) frequencies
    im1 = np.clip(fp.ifft2(fp.ifftshift(freq2)).real, 0, 255)  # clip pixel values after IFFT
    snrs_hp.append(signaltonoise(im1, axis=None))
    pylab.subplot(3, 4, idx), pylab.imshow(im1, cmap='gray'), pylab.axis('off')
    pylab.title('F = ' + str(l + 1))
    idx += 1

snr = signaltonoise(im, axis=None)
pylab.figure(figsize=[10, 6])
pylab.plot(lbs, snrs_hp, 'b.-')
pylab.plot(range(1, 25), [snr] * 24, 'r-')
pylab.legend(['SNR citra hasil HPF', 'SNR citra asli'])
pylab.xlabel('Cutoff Frequency for HPF')
pylab.ylabel('SNR (dB)')
pylab.grid()
pylab.show()
