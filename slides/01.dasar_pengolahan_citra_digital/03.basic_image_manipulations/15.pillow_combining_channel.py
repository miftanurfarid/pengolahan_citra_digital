"""
script ini akan melakukan penggabungan channel dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image

im = Image.open('../dataset/rose.png')

# memisahkan channel
ch_r, ch_g, ch_b = im.split()

# menggabungkan channel tapi di-swap
im = Image.merge('RGB', (ch_b, ch_g, ch_r))
im.show()
