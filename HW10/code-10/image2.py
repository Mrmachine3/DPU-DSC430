#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:17:08 2024

@author: payampourashraf
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import convolve

# Load a sample image
image = plt.imread('chicago.jpeg')
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Sobel filter for edge detection
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_x = convolve(gray_image, sobel_x)
edge_y = convolve(gray_image, sobel_y)

# Combine the horizontal and vertical edges
edges = np.sqrt(edge_x**2 + edge_y**2)

# Show the original, grayscale, and edge-detected images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')
plt.axis('off')

plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Assume 'image' is loaded as before and has shape (height, width, 3)
height, width, _ = image.shape

# Create a full white image
full_white = np.ones((height, width, 3)) * 255

# Create a full black image
full_black = np.zeros((height, width, 3))

# Create a full red image
full_red = np.zeros((height, width, 3))
full_red[:,:,0] = 255  # Set the red channel to maximum

full_blue = np.zeros((height, width, 3))
full_blue[:,:,2] = 255  # Set the red channel to maximum


# Display the images
plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(full_white.astype(np.uint8))
plt.title('Full White')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(full_black.astype(np.uint8))
plt.title('Full Black')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(full_blue.astype(np.uint8))
plt.title('Full Blue')
plt.axis('off')

plt.show()
