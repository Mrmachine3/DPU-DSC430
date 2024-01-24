#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 01/23/2024
# Path: /mnt/c/Users/atone/Desktop/DPU-DSC430/HW2/ARodriguez_HWtest_stem.py
# Usage: /usr/bin/python3 ARodriguez_HWtest_stem.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HWtest_stem
# Alternate CLI Usage: ./ARodriguez_HWtest_stem.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
from stemgraphic import stem_graphic

# FUNCTIONS

# MAIN PROGRAM
def main():
    data = [40, 37, 91, 44, 80, 72, 52, 29, 52, 29, 45, 70, 45, 53, 64, 23, 52, 60, 70, 42, 84, 23, 25, 32, 12, 90, 78, 72, 61, 20, 67, 73, 33, 64, 60, 14, 40, 41, 31, 59, 58, 22, 51, 41, 16, 52, 63, 20, 52, 41, 98, 38, 41, 44, 53, 60, 53, 72, 50, 85, 30, 15, 26, 64, 50, 53, 57, 49, 54, 57, 72, 72, 22, 31, 38, 62, 30, 66, 32, 59, 43, 49, 15, 25, 37, 59, 31, 38, 45, 46, 99, 34, 49, 61, 47, 74, 62, 27, 20, 58]

    print(f"length: {len(data)}")
    print(sorted(data))
    #fig, ax = stem_graphic(data)

if __name__ == "__main__":
    main()
