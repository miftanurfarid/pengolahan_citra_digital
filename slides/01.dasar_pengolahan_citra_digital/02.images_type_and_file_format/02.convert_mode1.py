"""
script ini akan melakukan converting mode
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from skimage.io import imread, imshow, show

im = imread('../dataset/ishihara.png', as_gray=True)
print(im.shape, im.dtype, type(im))
imshow(im)
show()
