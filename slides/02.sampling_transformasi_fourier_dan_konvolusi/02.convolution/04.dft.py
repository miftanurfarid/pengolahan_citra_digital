import numpy as np
from PIL import Image
import scipy.fftpack as fp
from matplotlib import pylab


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


im = np.array(Image.open('../dataset/flower.png').convert('L'))  # we shall work with grayscale image
snr = signaltonoise(im, axis=None)
print('SNR for the original image = ' + str(snr))
print(im.shape)
# SNR for the original image = 2.023722773801701

# now call FFT and IFFT
freq = fp.fft2(im)
im1 = fp.ifft2(freq).real
snr = signaltonoise(im1, axis=None)
print('SNR for the image obtained after reconstruction = ' + str(snr))

# SNR for the image obtained after reconstruction = 2.0237227738013224
assert (np.allclose(im, im1))  # make sure the forward and inverse FFT are close to each other
pylab.figure(figsize=(20, 10))
pylab.subplot(221), pylab.imshow(im, cmap='gray'), pylab.axis('off')
pylab.title('Original Image', size=20)
pylab.subplot(222), pylab.imshow(im1, cmap='gray'), pylab.axis('off')
pylab.title('Image obtained after reconstruction', size=20)

freq2 = fp.fftshift(freq)
freq3 = fp.fftshift(fp.fft2(im1))

pylab.subplot(223)
pylab.imshow((20 * np.log10(0.1 + freq2)).astype(int))
pylab.title('Spectrum of original image', size=20)

pylab.subplot(224)
pylab.imshow((20 * np.log10(0.1 + freq3)).astype(int))
pylab.title('Spectrum of reconstructed image', size=20)
pylab.show()
