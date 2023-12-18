from skimage.io import imread, imsave
from skimage.util import random_noise
from matplotlib import pylab
from skimage.restoration import denoise_bilateral, denoise_nl_means, estimate_sigma
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

do_plot = 1
im = imread('building_clean.jpg')
sigma = 0.155
im_noisy = random_noise(im, var=sigma ** 2)
#print(f'PSNR citra asli vs citra+noise: {np.round(peak_signal_noise_ratio(im,np.round(im_noisy*255).astype(np.uint8)),2)} dB')

imsave('building_noise.jpg', np.round(im_noisy*255).astype(np.uint8))

noisy = imread('building_noise.jpg')
print(f'PSNR citra asli vs citra+noise: {np.round(peak_signal_noise_ratio(im, noisy),2)} dB')

sigma_sp = 5  # [5, 10, 20]
sigma_col = 0.1  # [0.1, 0.25, 5]
im_rec = denoise_bilateral(noisy, sigma_color=sigma_col, sigma_spatial=sigma_sp, channel_axis=-1)
print(f'PSNR citra asli vs citra denoise bilateral: {np.round(peak_signal_noise_ratio(im,np.round(im_rec*255).astype(np.uint8)),2)} dB')

sigma_est = np.mean(estimate_sigma(noisy, channel_axis=-1))
patch_kw = dict(patch_size=5,  # 5x5 patches
                patch_distance=6,  # 13x13 search area
                channel_axis=-1)
denoise_fast = denoise_nl_means(noisy, h=0.8 * sigma_est, fast_mode=True, **patch_kw)
print(f'PSNR citra asli vs citra denoise non-linear means: {np.round(peak_signal_noise_ratio(im,np.round(denoise_fast*255).astype(np.uint8)),2)} dB')

if do_plot == 1:
    pylab.figure()
    pylab.subplot(131)
    pylab.title('Citra ber-noise')
    pylab.imshow(noisy)
    pylab.subplot(132)
    pylab.title('Citra hasil denoise bilateral')
    pylab.imshow(im_rec)
    pylab.subplot(133)
    pylab.title('Citra hasil denoise non-local means')
    pylab.imshow(denoise_fast)
    pylab.show()
