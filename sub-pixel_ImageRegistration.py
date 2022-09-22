# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:53:12 2021 Bangash-李忠勇 

@author: admin
"""

#import python packages which need to use.
import numpy as np
import matplotlib.pyplot as plt

##for utilites
from ipywidgets import interact, fixed
from IPython.display import clear_output   #for utilties

from skimage import data, io
from skimage.feature import register_translation
from skimage.feature.register_translation import _upsampled_dft
from scipy.ndimage import fourier_shift

#load the data
image = io.imread("G:/Medical Image Registration/Experimental results\Sub-pixel Image Registration/PATIENT_DICOM")
offset_image = io.imread("G:/Medical Image Registration/Experimental results\Sub-pixel Image Registration/PATIENT_DICOM")
#offset image translated by (-17.45, 18.75) in y and x

# subpixel precision
#Upsample factor 100 = images will be registered to within 1/100th of a pixel.
#Default is 1 which means no upsampling. 
shifted, error, diffphase = register_translation(image, offset_image, 100)
print(f"Detected subpixel offset (y,x): {shifted}")

from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(shifted[0], shifted[1]), mode='constant')
#plt.imshow(corrected_image)

#to plot the figure
fig= plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(offset_image, cmap='gray')
ax3.title.set_text('Corrected')

#finally show the figures
plt.show()
