import matplotlib.pyplot as plt
from skimage import io, transform, img_as_ubyte
import numpy as np

# Load gambar musim
musim_semi = io.imread('dataset//spring.jpg')
musim_panas = io.imread('dataset//summer.jpg')
musim_gugur = io.imread('dataset//fall.jpg')
musim_dingin = io.imread('dataset//fire.jpg')

# Resize gambar musim menjadi 612x408
musim_semi = transform.resize(musim_semi, (408, 612, 3))
musim_panas = transform.resize(musim_panas, (408, 612, 3))
musim_gugur = transform.resize(musim_gugur, (408, 612, 3))
musim_dingin = transform.resize(musim_dingin, (408, 612, 3))

# Gabungkan gambar musim menjadi satu citra
gambar_gabungan = np.zeros((816, 1224, 3), dtype=np.uint8)
gambar_gabungan[:408, :612, :] = (musim_semi * 255).astype(np.uint8)
gambar_gabungan[:408, 612:, :] = (musim_panas * 255).astype(np.uint8)
gambar_gabungan[408:, :612, :] = (musim_gugur * 255).astype(np.uint8)
gambar_gabungan[408:, 612:, :] = (musim_dingin * 255).astype(np.uint8)

# Simpan gambar hasil
io.imsave('dataset//hasil.jpg', img_as_ubyte(gambar_gabungan))

# Tampilkan gambar hasil
plt.imshow(gambar_gabungan)
plt.axis('off')
plt.show()
