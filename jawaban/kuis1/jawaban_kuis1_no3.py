from skimage.io import imread
import numpy as np
from scipy import ndimage
from matplotlib import pylab
import scipy.fftpack as fp
from skimage.color import rgb2gray

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)

image = imread('gabungan_4_musim.jpg')

kernel2 = np.array([[-1, -1, -1, -1, 8, -1, -1, -1, -1]]).reshape((3, 3, 1))

convolved_image2 = ndimage.convolve(image.astype(np.float_), kernel2, mode='nearest')
convolved_image2 = np.clip(convolved_image2, 0, 255).astype(np.uint8)

SNR_convolved_image2 = np.round(np.mean(signaltonoise(convolved_image2)),2)

# HPF
freq = fp.fft2(rgb2gray(image))
(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)
freq1 = np.copy(freq)
freq2 = fp.fftshift(freq1)

freq_cutoff = 1
while True:
    freq2[half_w - freq_cutoff:half_w + freq_cutoff + 1, half_h - freq_cutoff:half_h + freq_cutoff + 1] = 0
    image2 = np.clip(fp.ifft2(fp.ifftshift(freq2)).real, 0, 255)
    SNR_HPF = np.round(np.mean(signaltonoise(image2)), 2)
    print(SNR_HPF)
    if SNR_HPF <= 0.5:
        break
    freq_cutoff += 1

im1 = np.clip(fp.ifft2(fp.ifftshift(freq2)).real, 0, 255)

pylab.figure()
pylab.subplot(121)
pylab.title(f'Citra gabungan 4 musim hasil convolution terhadap kernel2. SNR = {SNR_convolved_image2}')
pylab.imshow(convolved_image2)
pylab.subplot(122)
pylab.title(f'Citra hasil HPF. SNR = {SNR_HPF}')
pylab.imshow(im1, cmap='gray')
pylab.show()
