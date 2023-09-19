"""
script ini akan menampilkan citra hasil dari penjumlahan 2 citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
from PIL.ImageChops import add

im1 = Image.open("../dataset/rose.png")
im2 = Image.open("../dataset/mountain.jpg").resize((im1.width, im1.height))
add(im1, im2).show()
