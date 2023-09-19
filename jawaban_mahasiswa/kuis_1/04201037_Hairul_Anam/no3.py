import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from skimage import io, color

# Load the image
image = io.imread('dataset/hasil.jpg')

# Convert the image to grayscale
gray_image = color.rgb2gray(image)

# Define the HPF kernel (you can adjust the kernel for your desired HPF effect)
hpf_kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

# Apply HPF filtering to the image
filtered_image = convolve2d(gray_image, hpf_kernel, mode='same', boundary='wrap')

# Calculate the SNR between the original and filtered images manually
original_mean = np.mean(gray_image)
noise = gray_image - filtered_image
noise_mean = np.mean(noise)
snr = 10 * np.log10((original_mean ** 2) / (noise_mean ** 2))

# Adjust the kernel and iterate until the desired SNR is achieved
desired_snr = 0.5  # Set your desired SNR here
while snr < desired_snr:
    # Adjust the HPF kernel (e.g., change values in the kernel)
    hpf_kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
    
    # Apply HPF filtering to the image
    filtered_image = convolve2d(gray_image, hpf_kernel, mode='same', boundary='wrap')

    # Calculate the SNR between the original and filtered images manually
    original_mean = np.mean(gray_image)
    noise = gray_image - filtered_image
    noise_mean = np.mean(noise)
    snr = 10 * np.log10((original_mean ** 2) / (noise_mean ** 2))

# Display the original and filtered images
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title(f'Filtered Image (SNR: {snr:.2f} dB)')
plt.axis('off')

plt.tight_layout()
plt.show()
