#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################

# Author: Anthony M. Rodriguez
# Date: 01/15/2024
# Path: /mnt/c/Users/atone/Desktop/DPU-DSC430/HW1/A.Rodriguez_HW2_coprime.py
# Usage: /usr/bin/python3 ARodriguez_HW1_coprime.py
# Alternate Usage: /usr/bin/python3 -m ARodriguez_HW1_coprime
# Alternate CLI Usage: ./ARodriguez_HW1_coprime.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430/blob/main/HW1/ARodriguez_HW1_coprime.py
# Video Explanation URL: https://youtu.be/qkcvdnN4Ly0
#
# Description:
# This program is used to derive a boolean result of whether two integers are
# coprime numbers, which are pairs of integers that do not have any common
# factors other than 1.

# LIBRARIES:

# FUNCTIONS:
def coprime(a,b):
    """Function returns the greatest common divisor or highest common factor
    of two numbers passed in as parameters by performing mathematical functions

    Args:
        a (str): An integer
        b (str): An integer

    Returns:
        (bool): returns whether the greatest common divisor is equal to 1

    """
    # Check if a is greater than b, if true then assign variable z the value of a, otherwise the value of b
    if a > b:
        z = a
    else:
        z = b

    # In a while loop check that z is divisible by both a and b to determine the least common multiple (LCM)
    while True:
        # Only break the while loop if both conditions are met, otherwise keep incrementing the value of z
        if (z % a == 0) and (z % b == 0):
            lcm = z
            break
        z += 1

    # The returned value implements a mathematical calculation to compute the greatest common divisor as an int
    return (a*b)/lcm

def coprime_test_loop():
    """Function executes a continous loop requiring input of two numbers that are
    casted to integer values, passed as parameters to the coprime function, and
    printed as a message indicating whether the two values entered are coprime
    numbers

    Within a while True loop, a user is able to press Ctrl + C to exit the
    program

    Args:
        a (str): A numeric string character casted to an integer type
        b (str): A numeric string character casted to an integer type

    Returns:
        (bool): returns True or False of the coprime function

    """
    while True:
        try:
            # Split user entry at the comma and unpack into variables a and b
            a,b = input(f"Enter two numbers seperated by a comma (press Ctrl + C, to quit): \n").split(",")

            if coprime(int(a),int(b)) == 1:
                result = True
            else:
                result = False

            # Printing f-string results with embedded coprime function and variables cast into int() function
            print(f"Are the numbers {a} and {b} coprime numbers? {result}\n")

        except KeyboardInterrupt:
            break

# MAIN PROGRAM:
def main():
    """Function call to invoke coprime_test_loop function"""
    coprime_test_loop()

# Primary function call that invokes the main function
if __name__ == "__main__":
    main()
