#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/06/2024
# Usage: /usr/bin/python3 ARodriguez_HW04_human_pyramid.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW04_human_pyramid
# Alternate CLI Usage: ./ARodriguez_HW04_human_pyramid.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/_W5l2R8Uxk4
#
# Description:
# This functions invokes the program logic to pass in all pairs of rows/columns
# represetning humans in the pyramid to the humanPyramid function to calculate
# the total weight being supported

# LIBRARIES

# FUNCTIONS
def humanPyramid(row,column):
    """This function calculates the total weight a human is supporting at each position in a human pyramid

    Args:
        row (int): the leve of humans arranged in the form of a  pyramid indexed by 0
        column (int): the position of the human from the left in each level indexed by 0

    Returns:
        int: the total weight supported by the human at each position of the table
    """
    # Initialize the starting weight of all human in pyramid
    w = 128

    # Base case: top person with no additional weigh to support
    if row == 0:
        return w
    # Leftmost person in the row
    elif column == 0:
        return w + humanPyramid(row - 1, column) / 2
    # Rightmost person in the row
    elif column == row:
        return w + humanPyramid(row - 1, column - 1) / 2
    # Person in the middle of the row
    else:
        return w + (humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column)) / 2

# MAIN PROGRAM FUNCTION
def main():
    """This functions invokes the program logic to pass in all pairs of
        rows/columnsrepresetning humans in the pyramid to the
        humanPyramid function to calculate the total weight being supported
    """
    pairs = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    i = 0
    while i != len(pairs):
        row = pairs[i][0]
        column = pairs[i][1]

        # Calculated weight for all humans supported by human at position (row,column)

        print(f"Total weight supported by human at position ({row},{column}): {humanPyramid(row,column)}")
        i += 1

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()