from skimage.io import imread
import numpy as np
from scipy import ndimage
from matplotlib import pylab

image = imread('gabungan_4_musim.jpg')

kernel1 = np.array([[0, -1, 0, -1, 5, -1, 0, -1, 0]]).reshape((3, 3, 1))

kernel2 = np.array([[-1, -1, -1, -1, 8, -1, -1, -1, -1]]).reshape((3, 3, 1))

kernel3 = np.array([[-2, -1, 0, -1, 1, 1, 0, 1, 2]]).reshape((3, 3, 1))

convolved_image1 = ndimage.convolve(image.astype(np.float_), kernel1, mode='nearest')
convolved_image1 = np.clip(convolved_image1, 0, 255).astype(np.uint8)

convolved_image2 = ndimage.convolve(image.astype(np.float_), kernel2, mode='nearest')
convolved_image2 = np.clip(convolved_image2, 0, 255).astype(np.uint8)

convolved_image3 = ndimage.convolve(image.astype(np.float_), kernel3, mode='nearest')
convolved_image3 = np.clip(convolved_image3, 0, 255).astype(np.uint8)

pylab.figure()
pylab.subplot(221)
pylab.title('Citra gabungan 4 musim')
pylab.imshow(image)
pylab.subplot(222)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel1')
pylab.imshow(convolved_image1)
pylab.subplot(223)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel2')
pylab.imshow(convolved_image2)
pylab.subplot(224)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel3')
pylab.imshow(convolved_image3)
pylab.show()