import matplotlib.pyplot as plt
from skimage import io, color, transform
from scipy.signal import convolve2d
import numpy as np
import math

# Load gambar hasil dari kodingan sebelumnya
gambar_hasil = io.imread('dataset//hasil.jpg')

# Kernels
kernel1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel3 = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

# Lakukan konvolusi dengan ketiga kernel
hasil_konvolusi1 = convolve2d(gambar_hasil[:, :, 0], kernel1, mode='same', boundary='wrap')
hasil_konvolusi2 = convolve2d(gambar_hasil[:, :, 1], kernel2, mode='same', boundary='wrap')
hasil_konvolusi3 = convolve2d(gambar_hasil[:, :, 2], kernel3, mode='same', boundary='wrap')

# Gabungkan hasil konvolusi menjadi citra baru
citra_konvolusi = np.zeros_like(gambar_hasil)
citra_konvolusi[:, :, 0] = hasil_konvolusi1
citra_konvolusi[:, :, 1] = hasil_konvolusi2
citra_konvolusi[:, :, 2] = hasil_konvolusi3

# Hitung SNR
def calculate_snr(original, filtered):
    original_energy = np.sum(original**2)
    noise_energy = np.sum((original - filtered)**2)
    snr = 10 * np.log10(original_energy / noise_energy)
    return snr

# Tampilkan citra sebelum dan sesudah konvolusi serta nilai SNR
plt.figure(figsize=(12, 6))

# Citra sebelum konvolusi
plt.subplot(1, 3, 1)
plt.imshow(gambar_hasil)
plt.title("Citra Sebelum Konvolusi")
plt.axis('off')

# Citra sesudah konvolusi
plt.subplot(1, 3, 2)
plt.imshow(citra_konvolusi)
plt.title("Citra Sesudah Konvolusi (HPF)")
plt.axis('off')

# Hitung dan tampilkan nilai SNR
original_gray = color.rgb2gray(gambar_hasil)
snr = calculate_snr(original_gray, citra_konvolusi[:, :, 0])
plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, f"SNR: {snr:.2f} dB", fontsize=12, ha='center')
plt.title("SNR")
plt.axis('off')

plt.show()
