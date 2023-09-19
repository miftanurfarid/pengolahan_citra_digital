"""
script ini akan melakukan perhitungan histogram pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')
pl = im.histogram()
plt.bar(range(256), pl[:256], color='r', alpha=0.5)
plt.bar(range(256), pl[256:2*256], color='g', alpha=0.4)
plt.bar(range(256), pl[2*256:], color='b', alpha=0.3)
plt.show()
