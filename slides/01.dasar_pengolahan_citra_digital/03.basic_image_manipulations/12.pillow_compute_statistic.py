"""
script ini akan melakukan perhitungan statistik pada citra dengan memanfaatkan library pillow.
penjelasan lebih detil dapat dibaca di file html atau python notebook yang telah disediakan
"""
from PIL import Image
import PIL.ImageStat as stat

im = Image.open('../dataset/rose.png')
s = stat.Stat(im)

# nilai maksimum dan minimum dari pixel di setiap channel RGB
print(s.extrema)

# jumlah pixel
print(s.count)

# rata-rata
print(s.mean)

# median
print(s.median)

# standar deviasi
print(s.stddev)
