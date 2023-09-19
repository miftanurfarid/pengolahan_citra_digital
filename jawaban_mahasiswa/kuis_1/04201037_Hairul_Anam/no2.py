import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# Load an example image (you can use your own image as well)
image = plt.imread('dataset/hasil.jpg')

# Define the convolution kernels
kernels = [
    np.array([[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]]),

    np.array([[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]]),

    np.array([[-2, -1, 0],
              [-1, 1, 1],
              [0, 1, 2]])
]

# Create a 2x2 subplot layout
plt.figure(figsize=(10, 8))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Apply each kernel to the image and display the results
for i, kernel in enumerate(kernels):
    # Split the image into its color channels (R, G, B)
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Perform convolution with the kernel on each color channel separately
    convolved_red_channel = convolve2d(red_channel, kernel, mode='same', boundary='wrap')
    convolved_green_channel = convolve2d(green_channel, kernel, mode='same', boundary='wrap')
    convolved_blue_channel = convolve2d(blue_channel, kernel, mode='same', boundary='wrap')

    # Combine the convolved color channels to form the final output image
    convolved_image = np.stack([convolved_red_channel, convolved_green_channel, convolved_blue_channel], axis=-1)

    # Display the convolved image
    plt.subplot(2, 2, i + 2)
    plt.imshow(convolved_image)
    plt.title(f'Kernel {i + 1}')
    plt.axis('off')

plt.tight_layout()
plt.show()
