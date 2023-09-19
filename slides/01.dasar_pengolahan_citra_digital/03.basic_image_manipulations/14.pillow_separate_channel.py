"""
script ini akan melakukan pemisahan channel dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""

from PIL import Image
import matplotlib.pylab as plt

im = Image.open('../dataset/rose.png')

# memisahkan channel RGB
ch_r, ch_g, ch_b = im.split()

plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.imshow(ch_r, cmap=plt.cm.Reds)
plt.axis('off')
plt.title('red')
plt.subplot(1, 3, 2)
plt.imshow(ch_g, cmap=plt.cm.Greens)
plt.axis('off')
plt.title('green')
plt.subplot(1, 3, 3)
plt.imshow(ch_b, cmap=plt.cm.Blues)
plt.axis('off')
plt.title('blue')
plt.tight_layout()
plt.show()
