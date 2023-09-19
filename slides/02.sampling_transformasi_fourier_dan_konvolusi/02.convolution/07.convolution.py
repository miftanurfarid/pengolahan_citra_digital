from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
from scipy import signal
from matplotlib import pylab

im = rgb2gray(imread('../dataset/flower.png')).astype(float)
print(np.max(im))
# 1.0
print(im.shape)
# (225, 225)
blur_box_kernel = np.ones((3, 3)) / 9
edge_laplace_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
im_blurred = signal.convolve2d(im, blur_box_kernel)
im_edges = np.clip(signal.convolve2d(im, edge_laplace_kernel), 0, 1)
fig, axes = pylab.subplots(ncols=3, sharex=True, sharey=True, figsize=(18, 6))
axes[0].imshow(im, cmap="gray")
axes[0].set_title('Original Image', size=20)
axes[1].imshow(im_blurred, cmap="gray")
axes[1].set_title('Box Blur', size=20)
axes[2].imshow(im_edges, cmap="gray")
axes[2].set_title('Laplace Edge Detection', size=20)
for ax in axes:
    ax.axis('off')
pylab.show()
