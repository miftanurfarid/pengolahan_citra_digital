from skimage.io import imread
from skimage.transform import resize
from matplotlib import pylab
import numpy as np
from scipy import signal

dataset = ["../../dataset/fire.jpg",
           "../../dataset/water.jpeg"]

# Jawaban No 1

im1 = imread(dataset[0])
print(f'Dimensi citra api adalah = {im1.shape[0]} x {im1.shape[1]}')
print(im1.shape)
im2 = imread(dataset[1])
print(f'Dimensi citra air adalah = {im2.shape[0]} x {im2.shape[1]}')
print(im2.shape)
new_size = [600, 900, 3]
im3 = np.ones(new_size)
im3[0:300, :, :] = resize(im1, new_size)[0:int(im3.shape[0]/2), :, :]
im3[300::, :, :] = resize(im2, new_size)[int(im3.shape[0]/2)::, :, :]
print(f'Dimensi citra api dan air = {im3.shape[0]} x {im3.shape[1]}')
print(im3.shape)

pylab.figure()
pylab.subplot(131)
pylab.title('Api')
pylab.imshow(im1)
pylab.subplot(132)
pylab.title('Api dan Air')
pylab.imshow(im3)
pylab.subplot(133)
pylab.title('Air')
pylab.imshow(im2)

# Jawaban No 2

kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
im3_conv = np.ones(im3.shape)

for i in range(3):
    im3_conv[:, :, i] = np.clip(np.real(signal.convolve2d(im3[..., i], kernel, mode='same', boundary="symm")),
                                0, 1)

pylab.figure()
pylab.subplot(121)
pylab.title('Citra sebelum difilter')
pylab.imshow(im3)
pylab.subplot(122)
pylab.title('Citra setelah difilter')
pylab.imshow(im3_conv)
pylab.show()
