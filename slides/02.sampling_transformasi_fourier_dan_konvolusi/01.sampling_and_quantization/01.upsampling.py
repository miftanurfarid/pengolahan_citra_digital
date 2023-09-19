from PIL import Image
import matplotlib.pylab as plt

im = Image.open("../dataset/flower_bali_58x50.jpg")
im1 = im.resize((im.width*5, im.height*5), Image.NEAREST) #upsampling
im2 = im.resize((im.width*5, im.height*5), Image.BILINEAR)

plt.subplot(131)
plt.imshow(im)
plt.title('Citra asli')
plt.subplot(132)
plt.imshow(im1)
plt.title('Citra upsampling nearest')
plt.subplot(133)
plt.imshow(im2)
plt.title('Citra upsampling bilinear')
plt.show()
