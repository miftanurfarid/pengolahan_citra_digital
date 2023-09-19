import numpy as np
from matplotlib import pylab
from skimage.io import imread
from skimage.transform import resize
from scipy import ndimage, fftpack
from skimage.color import rgb2gray


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


# Jawaban soal 1
dataset = ["../../dataset/spring.jpg",
           "../../dataset/summer.jpg",
           "../../dataset/fall.jpg",
           "../../dataset/winter.jpg"]

im1 = imread(dataset[0])
im2 = imread(dataset[1])
im3 = imread(dataset[2])
im4 = imread(dataset[3])
new_size = [600, 900, 3]
im5 = np.ones(new_size)
im5[0:int(im5.shape[0] / 2), 0:int(im5.shape[1] / 2), :] = resize(im1, new_size)[0:int(im5.shape[0] / 2),
                                                           0:int(im5.shape[1] / 2), :]
im5[0:int(im5.shape[0] / 2), int(im5.shape[1] / 2)::, :] = resize(im2, new_size)[0:int(im5.shape[0] / 2),
                                                           int(im5.shape[1] / 2)::, :]
im5[int(im5.shape[0] / 2)::, 0:int(im5.shape[1] / 2), :] = resize(im3, new_size)[int(im5.shape[0] / 2)::,
                                                           0:int(im5.shape[1] / 2), :]
im5[int(im5.shape[0] / 2)::, int(im5.shape[1] / 2)::, :] = resize(im4, new_size)[int(im5.shape[0] / 2)::,
                                                           int(im5.shape[1] / 2)::, :]

print(f'Dimensi citra musim semi adalah = {im1.shape[0]} x {im1.shape[1]}')
print(f'Dimensi citra musim panas adalah = {im2.shape[0]} x {im2.shape[1]}')
print(f'Dimensi citra musim gugur adalah = {im3.shape[0]} x {im3.shape[1]}')
print(f'Dimensi citra musim dingin adalah = {im4.shape[0]} x {im4.shape[1]}')
print(f'Dimensi citra gabungan semua musim adalah = {im5.shape[0]} x {im5.shape[1]}')

pylab.figure()
pylab.subplot(331)
pylab.title('Musim semi')
pylab.imshow(im1)
pylab.subplot(333)
pylab.title('Musim panas')
pylab.imshow(im2)
pylab.subplot(335)
pylab.title('Gabungan 4 musim')
pylab.imshow(im5)
pylab.subplot(337)
pylab.title('Musim gugur')
pylab.imshow(im3)
pylab.subplot(339)
pylab.title('Musim dingin')
pylab.imshow(im4)

# Jawaban soal 2
sharpen_kernel = np.array([0, -1, 0, -1, 5, -1, 0, -1, 0]).reshape((3, 3, 1))
edge_kernel = np.array([-1, -1, -1, -1, 8, -1, -1, -1, -1]).reshape((3, 3, 1))
emboss_kernel = np.array(np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])).reshape((3, 3, 1))
im_sharp = np.clip(ndimage.convolve(im5, sharpen_kernel, mode='nearest'), 0, 1)
im_edge = np.clip(ndimage.convolve(im5, edge_kernel, mode='nearest'), 0, 1)
im_emboss = np.clip(ndimage.convolve(im5, emboss_kernel, mode='nearest'), 0, 1)

pylab.figure()
pylab.subplot(221), pylab.imshow(im5)
pylab.title('Citra gabungan 4 musim')
pylab.subplot(222), pylab.imshow(im_sharp)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel 1')
pylab.subplot(223), pylab.imshow(im_edge)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel 2')
pylab.subplot(224), pylab.imshow(im_emboss)
pylab.title('Citra gabungan 4 musim hasil convolution terhadap kernel 3')

# Jawaban soal 3
im5 = rgb2gray(im5)
print(np.max(im5))
freq = fftpack.fft2(im5)
(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)
print(f"half_w = {half_w}")
print(f"half_h = {half_h}")
snrs_hp = []
lbs = list(range(1, 1000, 5))

for l in range(len(lbs)):
    freq1 = np.copy(freq)
    freq2 = fftpack.fftshift(freq1)
    freq2[half_w - lbs[l]:half_w + lbs[l] + 1,
    half_h - lbs[l]:half_h + lbs[l] + 1] = 0  # select all but the first lxl (low) frequencies
    print(f"\nwidth from: {half_w - lbs[l]} to : {half_w + lbs[l] + 1}")
    print(f"heigh from: {half_h - lbs[l]} to : {half_h + lbs[l] + 1}\n")
    im1 = np.clip(fftpack.ifft2(fftpack.ifftshift(freq2)).real, 0, 255)  # clip pixel values after IFFT
    snrs_hp.append(signaltonoise(im1, axis=None))
    print(signaltonoise(im1, axis=None))
    if signaltonoise(im1, axis=None) <= 0.5:
        print(f'SNR = {signaltonoise(im1, axis=None)}')
        print(f'frame = {lbs[l]}')
        break


pylab.figure()
pylab.subplot(121)
pylab.imshow(im_edge)
pylab.title(f'Citra hasil convolution terhadap kernel 2. SNR = {np.round(signaltonoise(im_edge, axis=None),2)}')
pylab.subplot(122)
print(np.max(im1))
print(np.max(im_edge))
pylab.imshow(im1, cmap='gray')
pylab.title(f'Citra hasil HPF. SNR = {np.round(signaltonoise(im1, axis=None),2)}')

pylab.show()
