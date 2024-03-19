#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:10:38 2024

@author: payampourashraf
"""

import numpy as np

A = np.array([1, 2, 3])
B = 2

# Add scalar B to array A
C = A + B  # Result is [3, 4, 5]

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 0, 1])

# Add 1D array B to each row of 2D array A
C = A + B  # Result is [[2, 2, 4], [5, 5, 7], [8, 8, 10]]


import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([1, 2])

# Multiply 2D array A by 1D array B
C = A * B  # Result is [[1, 4], [3, 8]]


import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([1, 2, 3])

# This will result in an error because the shapes are not compatible
# C = A + B
