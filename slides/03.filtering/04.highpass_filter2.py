from scipy import fftpack
import numpy as np
from PIL import Image
import scipy.fftpack as fp
from matplotlib import pylab


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


im = np.array(Image.open('./dataset/building.jpg').convert('L'))
freq = fp.fft2(im)
(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)
print(f"half_w = {half_w}")
print(f"half_h = {half_h}")
snrs_hp = []
lbs = list(range(1, 25, 2))
pylab.figure()
for l in range(len(lbs)):
    freq1 = np.copy(freq)
    freq2 = fftpack.fftshift(freq1)
    freq2[half_w - lbs[l]:half_w + lbs[l] + 1, half_h - lbs[l]:half_h + lbs[l] + 1] = 0  # select all but the first lxl (low) frequencies
    print(f"\nwidth from: {half_w - lbs[l]} to : {half_w + lbs[l] + 1}")
    print(f"heigh from: {half_h - lbs[l]} to : {half_h + lbs[l] + 1}\n")
    im1 = np.clip(fp.ifft2(fftpack.ifftshift(freq2)).real, 0, 255)  # clip pixel values after IFFT
    snrs_hp.append(signaltonoise(im1, axis=None))
    pylab.subplot(3, 4, l+1), pylab.imshow(im1, cmap='gray'), pylab.axis('off')
    pylab.title('F = ' + str(lbs[l] + 1))

pylab.subplots_adjust(wspace=0.1, hspace=0.2)

pylab.figure()
pylab.plot(lbs, snrs_hp, 'b.-')
pylab.xlabel('Cutoff Frequency for HPF', size=20)
pylab.ylabel('SNR', size=20)
pylab.show()
