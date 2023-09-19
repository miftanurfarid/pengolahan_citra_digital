"""
script ini memanfaatkan library pillow untuk melakukan hal-hal sebagai berikut:

1. membaca citra dari file
2. menyimpan citra ke file
3. menampilkan citra

penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image

# membaca citra, sediakan path atau directory yang tepat
im = Image.open("../dataset/rose.png")

# menampilkan dimensi dan metadata citra
print(im.width, im.height, im.mode, im.format, type(im))

# menampilkan citra melalui imageviewer default masing-masing operating system
im.show()

im_g = im.convert('L')  # mengubah citra RGB ke citra grayscale
im_g.save('../dataset/rose_gray.png')  # menyimpan gambar ke harddrive
im2 = Image.open("../dataset/rose_gray.png")
im2.show()  # membuka citra grayscale dari harddrive kemudian menampilkannya
