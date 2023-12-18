import numpy as np
from matplotlib import pyplot as plt
from skimage import io, transform

fall_image = io.imread('./fall.jpg')
spring_image = io.imread('./spring.jpg')
fire_image = io.imread('./fire.jpg')
summer_image = io.imread('./summer.jpg')

summer_array = np.array(summer_image)
spring_array = np.array(spring_image)
fire_array = np.array(fire_image)
fall_array = np.array(fall_image)

x1, y1, x2, y2 = 0, 0, 612, 408



summer_sliced = summer_array[y1:y2, x1:x2]
fall_sliced = fall_array[y1:y2, x1:x2]
spring_sliced = spring_array[y1:y2, x1:x2]
fire_sliced = fire_array[y1:y2, x1:x2]


#gambar_gabungan = np.zeros((816, 1224, 3), dtype=np.uint8)
#gambar_gabungan[:408, :612, :] = (summer_sliced * 255).astype(np.uint8)
#gambar_gabungan[:408, 612:, :] = (fall_sliced * 255).astype(np.uint8)
#gambar_gabungan[408:, :612, :] = (spring_sliced * 255).astype(np.uint8)
#gambar_gabungan[408:, 612:, :] = (fire_sliced * 255).astype(np.uint8)


plt.subplot(1, 4, 1)
plt.imshow(summer_sliced)
plt.title('Summer')


plt.subplot(1, 4, 2)
plt.imshow(fall_sliced)
plt.title('Fall')


plt.subplot(1, 4, 3)
plt.imshow(spring_sliced)
plt.title('Spring')


plt.subplot(1, 4, 4)
plt.imshow(fire_sliced)
plt.title('Fire')

plt.subplot(1,4,5)
plt.imshow(combined_image)
plt.title('Gabungan')

plt.show()