import matplotlib.pyplot as plt
from skimage import io, color, img_as_ubyte, filters, transform, util
import numpy as np
from scipy.signal import convolve2d
import math


gambar_hasil = io.imread('dataset//hasil.jpg')


gambar_hasil_gray = color.rgb2gray(gambar_hasil)


ambang = 0.5


gambar_hasil_binary = util.img_as_ubyte(gambar_hasil_gray > ambang)


kernel_hpf = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])


gambar_hasil_filtered = convolve2d(gambar_hasil_binary, kernel_hpf, mode='same')

# Hitung SNR
def calculate_snr(original, filtered):
    original_energy = np.sum(original**2)
    noise_energy = np.sum((original - filtered)**2)
    snr = 10 * np.log10(original_energy / noise_energy)
    return snr

# Citra asli yang telah diubah ukurannya
citra_asli = io.imread('dataset//hasil.jpg')
citra_asli_gray = color.rgb2gray(citra_asli)
citra_asli_gray_resized = transform.resize(citra_asli_gray, gambar_hasil_gray.shape)

# Hitung SNR antara citra asli dan citra hasil filtering
snr = calculate_snr(citra_asli_gray_resized, gambar_hasil_filtered)

# Tampilkan citra asli, citra hasil filtering, dan nilai SNR
plt.figure(figsize=(12, 6))

# Citra asli
plt.subplot(1, 3, 1)
plt.imshow(citra_asli_gray_resized, cmap='gray')
plt.title("Citra Asli")
plt.axis('off')

# Citra hasil filtering
plt.subplot(1, 3, 2)
plt.imshow(gambar_hasil_filtered, cmap='gray')
plt.title("Citra Hasil Filtering (Biner)")
plt.axis('off')

# Nilai SNR
plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, f"SNR: {snr:.2f} dB", fontsize=12, ha='center')
plt.axis('off')

plt.show()
