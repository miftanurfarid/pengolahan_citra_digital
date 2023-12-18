from skimage.io import imread
from skimage.util import img_as_float
from matplotlib import pylab
from skimage.morphology import binary_erosion, binary_dilation


im = imread('human.png')
pylab.gray()
pylab.subplot(131)
pylab.title('Citra asli')
pylab.imshow(im)

im = img_as_float(im[..., 3])
threshold = 0.5
im[im <= threshold] = 0
im[im > threshold] = 1
im_eros = binary_erosion(im) - im
pylab.subplot(132)
pylab.title('Citra hasil binary erosion morphological')
pylab.imshow(im_eros)

im_dila = im-binary_dilation(im)
pylab.subplot(133)
pylab.title('Citra hasil binary dilation morphological')
pylab.imshow(im_dila)
pylab.show()
