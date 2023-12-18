from skimage.io import imread, imsave
from skimage.transform import resize
from matplotlib import pylab
import numpy as np

image1 = imread('spring.jpg')
image2 = imread('summer.jpg')
image3 = imread('fall.jpg')
image4 = imread('winter.jpg')

image1_new = resize(image1, (600, 900) )
image2_new = resize(image2, (600, 900) )
image3_new = resize(image3, (600, 900) )
image4_new = resize(image4, (600, 900) )

half_height = int(image1_new.shape[0]/2)
print(half_height)
half_width = int(image1_new.shape[1]/2)
print(half_width)

image5 = image1_new
image5[0:half_height, half_width+1:image5.shape[1]] = image2_new[0:half_height,half_width+1:image2.shape[1]]
image5[half_height+1:image5.shape[0], 0:half_width] = image3_new[half_height+1:image5.shape[0], 0:half_width]
image5[half_height+1:image5.shape[0], half_width+1:image5.shape[1]] = image4_new[half_height+1:image5.shape[0], half_width+1:image5.shape[1]]

image5 = np.uint8(image5 * 255)
imsave('gabungan_4_musim.jpg', image5)


pylab.figure()
pylab.subplot(331)
pylab.imshow(image1)
pylab.title('Musim semi')
pylab.subplot(333)
pylab.imshow(image2)
pylab.title('Musim panas')
pylab.subplot(335)
pylab.imshow(image5)
pylab.title('Gabungan empat musim')
pylab.subplot(337)
pylab.imshow(image3)
pylab.title('Musim gugur')
pylab.subplot(339)
pylab.imshow(image4)
pylab.title('Musim dingin')
pylab.show()
