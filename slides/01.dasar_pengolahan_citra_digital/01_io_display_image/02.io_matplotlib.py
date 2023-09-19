"""
script ini memanfaatkan library matplotlib untuk melakukan hal-hal sebagai berikut:

1. membaca citra dari file
2. menyimpan citra ke file
3. menampilkan citra melalui imageviewer default masing-masing operating system

penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

import matplotlib.image as mpimg
import matplotlib.pylab as plt

# membaca citra dari harddrive sebagai sebuah numpy ndarray
im = mpimg.imread("../dataset/mountain.png")

# menampilkan dimensi dan metadata citra
print(im.shape, im.dtype, type(im))

# menampilkan citra melalui qt
plt.figure()
plt.imshow(im)
plt.title('Citra asli')

# mengubah citra menjadi lebih gelap kemudian
# menyimpan citra yang gelap tersebut ke harddrive
im1 = im.copy()
im1[im1 < 0.6] = 0
plt.figure()
plt.axis('off')
plt.tight_layout()
plt.imshow(im1)
plt.title('Citra lebih gelap - ditampilkan langsung tanpa disimpan')
plt.savefig("../dataset/mountain_dark.png")

# membaca dan menampilkan citra gelap yang sudah disimpan sebelumnya
im2 = mpimg.imread("../dataset/mountain_dark.png")
plt.figure()
plt.imshow(im2)
plt.title('Citra lebih gelap - hasil membaca file yang kedua')
plt.show()
