"""
script ini akan melakukan converting file format dari png ke jpg.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image

# convert from png to jpg
# RGB
im = Image.open("../dataset/rose.png")
print(im.mode)
im.save("./dataset/rose.jpg")

"""
Jika file PNG memiliki RGBA mode, maka kita perlu mengubahnya
terlebih dahulu menjadi RGB mode sebelum menyimpannya sebagai JPG
"""
im = Image.open("./dataset/mountain.png")
print(im.mode)

# mengubah ke RGB kemudian menyimpan citra ke harddrive
im.convert('RGB').save("./dataset/mountain.jpg")
