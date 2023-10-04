from matplotlib import pylab
from matplotlib.colors import LogNorm
import numpy as np
import scipy.fftpack as fp


im = pylab.imread('../dataset/moonlanding.png').astype(float)
im_fft = fp.fft2(im)
# Copy the original spectrum and truncate coefficients.
# Define the fraction of coefficients (in each direction) to keep as
keep_fraction = 0.1
im_fft2 = im_fft.copy()
# Set r and c to the number of rows and columns of the array.
r, c = im_fft2.shape
# Set all rows to zero with indices between r*keep_fraction and r*(1-keep_fraction)
im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
# Similarly with the columns
im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0
im_new = fp.ifft2(im_fft2).real

pylab.figure(figsize=(9, 7))
pylab.subplot(221)
pylab.title('Citra noisy asli', size=10)
pylab.imshow(im, cmap='gray')
pylab.subplot(222)
pylab.title('Spectrum citra noisy', size=10)
pylab.imshow(np.abs(fp.fftshift(im_fft)), norm=LogNorm(vmin=5), cmap='afmhot')
pylab.colorbar()
pylab.subplot(223)
pylab.title('Spectrum citra noisy asli setelah difilter', size=10)
pylab.imshow(np.abs(fp.fftshift(im_fft2)), norm=LogNorm(vmin=5), cmap='afmhot')
pylab.colorbar()
pylab.subplot(224)
pylab.title('Citra hasil filter', size=10)
pylab.imshow(im_new, cmap='gray')
pylab.show()
