import numpy as np
from matplotlib import pylab
from skimage.io import imread
import scipy.fftpack as fp

im1 = np.mean(imread("../dataset/rose.jpg"), axis=2) / 255
freq1 = fp.fftshift(fp.fft2(im1.astype(float)))
print(im1.shape)
# add periodic noise to the image
im2 = np.copy(im1)
for n in range(im2.shape[1]):
    im2[:, n] += np.cos(0.1 * np.pi * 0.5 * n)

freq2 = fp.fftshift(fp.fft2(im2.astype(float)))  # noisy spectrum

pylab.figure(figsize=[10, 6])
pylab.subplot(2, 2, 1), pylab.imshow(im1, cmap='gray')
pylab.title('Citra asli', size=10)
pylab.subplot(2, 2, 2), pylab.imshow((20 * np.log10(0.1 + freq1)).astype(int), cmap='gray')
pylab.title('Spectrum citra asli', size=10)
pylab.subplot(2, 2, 3), pylab.imshow(im2, cmap='gray')
pylab.title('Citra setelah ditambahkan Sinusoidal Noise', size=10)
pylab.subplot(2, 2, 4), pylab.imshow((20 * np.log10(0.1 + freq2)).astype(int), cmap='gray')
pylab.title('Spectrum citra setelah ditambahkan Sinusoidal Noise', size=10)
pylab.xticks(np.arange(0, im1.shape[1], 80))
pylab.yticks(np.arange(0, im1.shape[0], 54))
pylab.tight_layout()

xcf = 1
ycf = 1
freq3 = np.copy(freq2)
freq3[int(im1.shape[0] / 2) - xcf:int(im1.shape[0] / 2) + xcf, :int(im1.shape[1] / 2) - ycf] = freq3[int(
    im1.shape[0] / 2) - xcf:int(im1.shape[0] / 2) + xcf, int(im1.shape[1] / 2) + ycf:] = 0
im3 = fp.ifft2(fp.ifftshift(freq3)).real
pylab.figure()
pylab.imshow(im3, cmap='gray'), pylab.title('Rekonstruksi setelah BSF')
pylab.show()
