#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/14/2024
# Usage: /usr/bin/python3 ARodriguez_HW09_numpy_intro.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW09_numpy_intro
# Alternate CLI Usage: ./ARodriguez_HW09_numpy_intro.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/mCHJWQD2fJw
#
# Description:
# This script demonstrates basic functionalities of the NumPy library,
# including array creation, reshaping, random array generation, and
# various mathematical operations. It serves as an introduction to NumPy
# and showcases its capabilities for numerical computing tasks.

# LIBRARIES
import numpy as np

# FUNCTIONS

# MAIN PROGRAM FUNCTION
def main():
    a = np.arange(0,100)
    print(f"Variable a:\n{a}\n")

    b = np.arange(0,100,10)
    print(f"Variable b:\n{b}")

    c = np.linspace(0,10,101)
    print(f"\nVariable c:\n{c}")

    d = np.random.random((10,10))
    print(f"\nVariable d:\n{d}")

    a = a.reshape(10,10)
    print(f"\nReshaped variable a:\n{a}")

    print(f"\nResult of 'a[4,5]':")
    print(f"{a[4,5]}")

    print(f"\nResult of 'a[4]':")
    print(f"{a[4]}")

    print(f"\nResult of sum of 'd':")
    print(f"{d.sum()}")

    print(f"\nResult of max of 'a':")
    print(f"{a.max()}")

    print(f"\nResult of transpose of 'b':")
    print(f"{b.transpose()}")

    print(f"\nResult of adding 'a' and 'd':")
    print(f"{a+d}")

    print(f"\nResult of multiplying 'a' and 'd':")
    print(f"{a*d}")

    print(f"\nResult of computing the dot product of 'a' and 'd':")
    print(f"{np.dot(a,d)}")

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()