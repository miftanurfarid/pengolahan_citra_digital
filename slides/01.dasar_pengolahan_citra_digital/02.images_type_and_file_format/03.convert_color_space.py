"""
script ini akan melakukan converting color space dari RGB ke HSV
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import color

im = imread("../dataset/rose.png")
im_hsv = color.rgb2hsv(im)
plt.figure(figsize=(10,8))
plt.subplot(131), plt.imshow(im_hsv[...,0]), plt.title('h', size=20),
plt.axis('off')
plt.gray()
plt.subplot(132), plt.imshow(im_hsv[...,1]), plt.title('s', size=20),
plt.axis('off')
plt.gray()
plt.subplot(133), plt.imshow(im_hsv[...,2]), plt.title('v', size=20),
plt.axis('off')
plt.gray()
plt.show()
