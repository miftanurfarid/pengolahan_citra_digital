import timeit
import numpy as np
from skimage.io import imread
from scipy import signal
from matplotlib import pylab

im = np.mean(imread('../dataset/building.jpg'), axis=2)
# 2D Gaussian kernel of size 11x11 with σ = 3
gauss_kernel = np.outer(signal.windows.gaussian(11, 3), signal.windows.gaussian(11, 3))
im_blurred1 = signal.convolve(im, gauss_kernel, mode="same")
im_blurred2 = signal.fftconvolve(im, gauss_kernel, mode='same')

pylab.figure(figsize=[8, 5])
pylab.gray()
pylab.subplot(131), pylab.imshow(im), pylab.title('Citra asli')
pylab.subplot(132), pylab.imshow(im_blurred1), pylab.title('Hasil convolved()')
pylab.subplot(133), pylab.imshow(im_blurred2), pylab.title('Hasil fftconvolved()')


# perbandingan waktu komputasi
def wrapper_convolve(func):
    def f_wrapped_convolve():
        return func(im, gauss_kernel, mode="same")

    return f_wrapped_convolve


wrapped_convolve = wrapper_convolve(signal.convolve)
wrapped_fftconvolve = wrapper_convolve(signal.fftconvolve)

times1 = timeit.repeat(wrapped_convolve, number=1, repeat=100)
times2 = timeit.repeat(wrapped_fftconvolve, number=1, repeat=100)

data = [times1, times2]

pylab.figure(figsize=[8, 5])
box = pylab.boxplot(data, patch_artist=True)  # notch=True,
colors = ['cyan', 'pink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
pylab.xticks(np.arange(3), ('', 'convolve', 'fftconvolve'))
pylab.yticks(fontsize=12)
pylab.xlabel('scipy.signal convolution methods')
pylab.ylabel('time taken to run')
pylab.show()
