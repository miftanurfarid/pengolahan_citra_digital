from scipy import signal
from skimage.io import imread
import numpy as np
from matplotlib import pylab

im = imread('../dataset/flower_bali.jpg') / 255  # scale each pixel value in [0,1]
print(np.max(im))
print(im.shape)
emboss_kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
edge_schar_kernel = np.array([[-3 - 3j, 0 - 10j, +3 - 3j], [-10 + 0j, 0 + 0j,
                                                            +10 + 0j], [-3 + 3j, 0 + 10j, +3 + 3j]])
im_embossed = np.ones(im.shape)
im_edges = np.ones(im.shape)
for i in range(3):
    im_embossed[..., i] = np.clip(signal.convolve2d(im[..., i],
                                                    emboss_kernel,
                                                    mode='same', boundary="symm"),0, 1)

for i in range(3):
    im_edges[:, :, i] = np.clip(np.real(signal.convolve2d(im[..., i], edge_schar_kernel, mode='same', boundary="symm")),
                                0, 1)

fig, axes = pylab.subplots(ncols=3, figsize=(20, 30))
axes[0].imshow(im)
axes[0].set_title('Original Image', size=20)
axes[1].imshow(im_embossed)
axes[1].set_title('Embossed Image', size=20)
axes[2].imshow(im_edges)
axes[2].set_title('Schar Edge Detection', size=20)
for ax in axes:
    ax.axis('off')
pylab.show()
