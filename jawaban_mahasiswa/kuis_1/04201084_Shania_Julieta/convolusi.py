import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.signal import convolve2d

# Membaca citra hasil dari Soal 1
image = io.imread('dataset/hasil.jpg')

# Kernel-kernel yang akan digunakan untuk konvolusi
kernel1 = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

kernel2 = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

kernel3 = np.array([[-1, -1, -1],
                    [-1,  9, -1],
                    [-1, -1, -1]])

# Melakukan konvolusi dengan kernel pertama
convolved_image1 = convolve2d(image, kernel1, mode='same', boundary='wrap')

# Melakukan konvolusi dengan kernel kedua
convolved_image2 = convolve2d(image, kernel2, mode='same', boundary='wrap')

# Melakukan konvolusi dengan kernel ketiga
convolved_image3 = convolve2d(image, kernel3, mode='same', boundary='wrap')

# Menampilkan citra sebelum dan sesudah konvolusi
plt.figure(figsize=(15, 5))

# Citra sebelum konvolusi
plt.subplot(141)
plt.imshow(image)
plt.title('Citra Sebelum Konvolusi')
plt.axis('off')

# Citra setelah konvolusi dengan kernel pertama
plt.subplot(142)
plt.imshow(convolved_image1, cmap='gray')
plt.title('Citra Setelah Konvolusi (Kernel 1)')
plt.axis('off')

# Citra setelah konvolusi dengan kernel kedua
plt.subplot(143)
plt.imshow(convolved_image2, cmap='gray')
plt.title('Citra Setelah Konvolusi (Kernel 2)')
plt.axis('off')

# Citra setelah konvolusi dengan kernel ketiga
plt.subplot(144)
plt.imshow(convolved_image3, cmap='gray')
plt.title('Citra Setelah Konvolusi (Kernel 3)')
plt.axis('off')

plt.tight_layout()
plt.show()