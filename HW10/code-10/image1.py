#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:13:20 2024

@author: payampourashraf
"""

import matplotlib.pyplot as plt
import numpy as np

# Load a sample image
image = plt.imread('chicago.jpeg')

# Convert the image to grayscale
# The grayscale value can be calculated as the weighted sum of the R, G, and B values
# 0.2989 * R + 0.5870 * G + 0.1140 * B
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Show the original image
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gray_image + image)
plt.title('broadcasting Image')
plt.axis('off')

# Show the grayscale image
plt.subplot(1, 3, 3)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.show()
