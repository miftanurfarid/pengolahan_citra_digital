import matplotlib.pyplot as plt
from PIL import Image
from skimage import io, transform, img_as_ubyte
# Load the original four images
image1 = Image.open('dataset/fire.jpg')
image2 = Image.open('dataset/spring.jpg')
image3 = Image.open('dataset/summer.jpg')
image4 = Image.open('dataset/fall.jpg')

# Create subplots to display the original images
plt.subplot(331)
plt.imshow(image1)
plt.title('Image 1')
plt.axis('off')

plt.subplot(333)
plt.imshow(image2)
plt.title('Image 2')
plt.axis('off')

plt.subplot(337)
plt.imshow(image3)
plt.title('Image 3')
plt.axis('off')

plt.subplot(339)
plt.imshow(image4)
plt.title('Image 4')
plt.axis('off')

# Slice the four images
slice_width = 300  # Adjust the slice dimensions as needed
slice_height = 200

sliced_image1 = image1.crop((0, 0, slice_width, slice_height))
sliced_image2 = image2.crop((0, 0, slice_width, slice_height))
sliced_image3 = image3.crop((0, 0, slice_width, slice_height))
sliced_image4 = image4.crop((0, 0, slice_width, slice_height))

# Combine the sliced images into one image
combined_image = Image.new('RGB', (2 * slice_width, 2 * slice_height))
combined_image.paste(sliced_image1, (0, 0))
combined_image.paste(sliced_image2, (slice_width, 0))
combined_image.paste(sliced_image3, (0, slice_height))
combined_image.paste(sliced_image4, (slice_width, slice_height))

io.imsave('dataset/hasil.jpg', img_as_ubyte(combined_image))
# Display the combined image in subplot 335
plt.subplot(335)
plt.imshow(combined_image)
plt.title('Combined Image')
plt.axis('off')

# Show the subplots
plt.tight_layout()
plt.show()
