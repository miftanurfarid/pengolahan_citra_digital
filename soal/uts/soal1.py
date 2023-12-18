#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 02:27:50 2023

@author: fafa
"""

from skimage.io import imread
from skimage import exposure
from matplotlib import pylab
import numpy as np

im = imread('lowlight.jpg')
im_r = im[:, :, 0]
im_g = im[:, :, 1]
im_b = im[:, :, 2]

# histogram equalization
im_r_eq = exposure.equalize_hist(im_r)
im_g_eq = exposure.equalize_hist(im_g)
im_b_eq = exposure.equalize_hist(im_b)
im_eq = np.ones(im.shape)
im_eq[:, :, 0] = im_r_eq
im_eq[:, :, 1] = im_g_eq
im_eq[:, :, 2] = im_b_eq

# histogram adaptive equalization
im_r_ad = exposure.equalize_adapthist(im_r, clip_limit=0.03)
im_g_ad = exposure.equalize_adapthist(im_g, clip_limit=0.03)
im_b_ad = exposure.equalize_adapthist(im_b, clip_limit=0.03)
im_ad = np.ones(im.shape)
im_ad[:, :, 0] = im_r_ad
im_ad[:, :, 1] = im_g_ad
im_ad[:, :, 2] = im_b_ad

# plotting
pylab.figure(figsize=[18,8])
pylab.subplot(231)
pylab.imshow(im)
pylab.title('Citra asli', size=10)
pylab.subplot(232)
pylab.imshow(im_eq)
pylab.title('Citra hasil histogram equalization', size=10)
pylab.subplot(233)
pylab.imshow(im_ad)
pylab.title('Citra hasil histogram adaptive equalization', size=10)
pylab.subplot(234)
pylab.hist(im.ravel(), color='g')
pylab.title('Histogram citra asli', size=10)
pylab.subplot(235)
pylab.hist(im_eq.ravel(), color='g')
pylab.title('Histogram citra hasil histogram equalization', size=10)
pylab.subplot(236)
pylab.hist(im_ad.ravel(), color='g')
pylab.title('Histogram citra hasil histogram adaptive equalization', size=10)
pylab.show()
