#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:10:25 2024

@author: payampourashraf
"""

import numpy as np

# Creating a 3D array with shape (4, 3, 2)
array_3d = np.array([[[1, 2], [3, 4], [5, 6]],
                     [[7, 8], [9, 10], [11, 12]],
                     [[13, 14], [15, 16], [17, 18]],
                     [[19, 20], [21, 22], [23, 24]]])

# Accessing elements along axis 0
for sub_array in array_3d:
    print(sub_array)
    print("payam")

import numpy as np

# Example 3D array
array_3d = np.array([[[1, 2], [3, 4], [5, 6]],
                     [[7, 8], [9, 10], [11, 12]],
                     [[13, 14], [15, 16], [17, 18]],
                     [[19, 20], [21, 22], [23, 24]]])

# Accessing elements along axis 2
slice_index = 0  # For example, select the first 2D slice
row_index = 1    # For example, select the second row within that slice
for element in array_3d[slice_index][row_index]:
    print(element)


import numpy as np

# Assuming array_3d is already defined as a 3D NumPy array
for i in range(array_3d.shape[0]):  # Loop over axis 0
    for j in range(array_3d.shape[1]):  # Loop over axis 1
        print(array_3d[i, j, :])  # Accessing all elements along axis 2 at once

