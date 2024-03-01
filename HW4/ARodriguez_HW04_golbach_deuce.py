#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/06/2024
# Usage: /usr/bin/python3 ARodriguez_HW04_golbach_deuce.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW04_golbach_deuce
# Alternate CLI Usage: ./ARodriguez_HW04_golback_deuce.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/gkPQANWts6o
#
# Description:
# This program generates a list of random numbers between 1 and 100 and
# prints the sum of any two numbers in the list when equal to the sum
# entered by the user
#
# Resources:
# https://skerritt.blog/big-o/#%F0%9F%A7%AE-how-to-calculate-big-o-notation-for-our-own-algorithms-with-examples

# LIBRARIES
import random

# FUNCTIONS
def generate_number_list(length,min,max):
    """This function returns a list of randomly selected numbers between
        lower and upper limits

    Args:
        length (int): desired length of list entered by user
        min (int): the lower limit for the range to select random integers
        max (int): the upper limit for the range to select random integers

    Returns:
        list: a list of randomly selected numbers between lower and upper limits
    """
    rand_list = []

    for i in range(length):
        rand_list.append(random.randint(min,max))

    return rand_list

def binary_search(randlist,low,high,num):
    """This function performs a binary search to find the value 'num' in 'rand_list'
        denoted by the lower and upper bounds of the list upon each iteration

    Args:
        randlist (list): a list of randomly generated integers
        low (int): the lower bound of the search range
        high (int): the upper bound of the search range
        num (int): _description_

    Returns:
        int: an integer representing whether a searched value was found
    """
    m = 0
    # Keep iterating when lower bound is less than or equal to upper bound 
    while (low <= high):
        # Derive the midpoint of the range
        m = (high + low)//2
        # Check if num is found at midpoint
        if (randlist[m] == num):
            return 1
        # if num is greater, ignore left half
        if (randlist[m] < num):
            low = m + 1
        # if num is smaller, ignore right half
        else:
            high = m - 1
    # Otherwise number is not present
    return 0

# MAIN PROGRAM FUNCTION
def main(min,max):

    while True:
        try:
            # Ask end-user to enter a positive number
            length = int(input(f"Enter a length: "))
            sum = int(input(f"Enter a sum: "))

            # Generate a list of random number of desired length between min and max
            rand_list = sorted(generate_number_list(length,min,max))
            size = len(rand_list)
            print(f"{rand_list}")

            # Initialize starting position to search 'rand_list'
            i = 0
            
            while i < (size-1):
                # Set value of num equal to the result of sum minus the value in position i of 'rand_list'
                num = sum - rand_list[i]

                # Invoke binary_search function to find if two numbers summed yield the expected sum
                if(binary_search(rand_list, i+1, size, num) == 1):
                    print(f"{sum} = {num} + {sum - num}")
                    return 1
                i +=1
            print(f"No two numbers in list yield {sum}")
            return 1

        except KeyboardInterrupt:
            print(f"")
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main(1,100)