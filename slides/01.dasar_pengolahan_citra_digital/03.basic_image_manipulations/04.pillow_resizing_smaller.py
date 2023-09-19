"""
script ini akan melakukan resizing terhadap citra menjadi lebih kecil dengan menggunakan library pillow
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/flower_bali.jpg')
print(im.width, im.height)

# resizing menggunakan lanczos interpolation
im_small = im.resize((im.width//5, im.height//5), Image.LANCZOS)
print(im_small.width, im_small.height)

# bandingkan hasil resizing
plt.subplot(121)
plt.imshow(im)
plt.title('citra asli')
plt.subplot(122)
plt.imshow(im_small)
plt.title('citra hasil resizing')
plt.show()
