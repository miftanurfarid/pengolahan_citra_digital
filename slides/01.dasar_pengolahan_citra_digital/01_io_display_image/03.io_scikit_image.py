"""
script ini memanfaatkan library scikit-image untuk melakukan hal-hal sebagai berikut:

1. membaca citra dari file
2. menyimpan citra ke file
3. menampilkan citra

penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread, imshow, show, imsave
from skimage import color
import numpy as np

# membaca citra dari harddrive, berikan directory yg tepat
im = imread("../dataset/flower.png")

# menampilkan dimensi dan metadata citra
print(im.shape, im.dtype, type(im))

# menampilkan citra
imshow(im)
show()

# merubah citra dari RGB ke HSV kemudian menyimpannya
hsv = color.rgb2hsv(im)  # dari RGB ke HSV
hsv[:, :, 1] = 0.5  # mengubah saturation
im1 = color.hsv2rgb(hsv)  # from HSV back to RGB
im1 = np.uint8(im1 * 255)  # karena type float, perlu diubah ke 8-bit unsigned int
imsave("../dataset/flower_hsv.png", im1)  # menyimpan citra ke harddrive
