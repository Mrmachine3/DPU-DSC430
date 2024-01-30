#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 01/29/2024
# Path: /mnt/c/Users/atone/Desktop/DPU-DSC430/HW3/ARodriguez_HWgoldbach_conjecture.py
# Usage: /usr/bin/python3 ARodriguez_HWgoldbach_conjecture.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HWgoldbach_conjecture
# Alternate CLI Usage: ./ARodriguez_HWgoldbach_conjecture.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES

# FUNCTIONS
def is_prime(n):
    """Function to check if parameter 'n' is a prime number

    Args:
        n (int): an integer that will be checked if it is a prime number

    Returns:
        (bool): boolean value indicating whether 'n' is a prime number, or not
    """
    prime = True

    if n < 2:
        prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                prime = False
    return prime

def generate_primes(a,b):
    """Function to generate list of prime numbers between a range

    Args:
        a (int): the lower limit of a range
        b (int): the upper limit of a range

    Returns:
        primes (list): a list of calculated prime numbers between the upper and
        lower limits
    """
    primes = [x for x in range(a,b+1) if is_prime(x)]

    return primes

# MAIN PROGRAM FUNCTION
def main(a,b):
    """Function to iterate over a range of numbers and solely display the sum
    of two prime which results in an event number greater than 2

    Args:
        a (int): the lower limit of a range
        b (int): the upper limit of a range

    Returns:
        (str): A message to console displaying the sum of two prime numbers
        yielding an even number

    """
    primes = generate_primes(a,b)

    # Loop through lower and upper limits of range
    for n in range(a,b+1):
        # continue loop for all even values within the range greater than 4
        if n >= 4 and n % 2 == 0:

            # Loop through all positions of the 'primes' list
            for i in primes:
                # Loop through all positions of the 'primes' list
                for j in primes:
                    # validate that sum of two values in variable 'i' and 'j'
                    # equal an even value greater than 4 in the range
                    if n == (i + j):
                        # Display the sume of values equal to all even numbers
                        # within the range
                        print(f"{n} = {i} + {j}")


# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main(1,100)
