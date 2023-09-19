"""
script ini akan melakukan geometric transformations terhadap citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')

im_refl = im.transpose(Image.FLIP_LEFT_RIGHT)

im_45 = im.rotate(45)

im_affine = im.transform((int(1.4 * im.width), im.height), Image.AFFINE, data=(1, -0.5, 0, 0, 1, 0))

params = [1, 0.1, 0, -0.1, 0.5, 0, -0.005, -0.001]
im_pers = im.transform((im.width // 3, im.height), Image.PERSPECTIVE, params, Image.BICUBIC)

plt.subplot(231)
plt.imshow(im)
plt.title('Citra asli')
plt.subplot(232)
plt.imshow(im_refl)
plt.title('Citra hasil reflect')
plt.subplot(233)
plt.imshow(im_45)
plt.title('Citra hasil rotate')
plt.subplot(234)
plt.imshow(im_affine)
plt.title('Citra hasil affine transform')
plt.subplot(235)
plt.imshow(im_pers)
plt.title('Citra hasil perspective transform')
plt.show()
