"""
script ini akan melakukan resizing terhadap citra menjadi lebih besar dengan menggunakan library pillow
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/flower_bali_58x50.jpg')
print(im.width, im.height)

# resizing menggunakan bi-linear interpolation
im_large = im.resize((im.width*5, im.height*5), Image.BILINEAR)
print(im_large.width, im_large.height)

# bandingkan hasil resizing
plt.subplot(121)
plt.imshow(im)
plt.title('citra asli')
plt.subplot(122)
plt.imshow(im_large)
plt.title('citra hasil resizing')
plt.show()
