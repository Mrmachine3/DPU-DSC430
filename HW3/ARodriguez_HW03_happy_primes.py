#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 01/30/2024
# Usage: /usr/bin/python3 ARodriguez_HW03_happy_primes.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW03_happy_primes
# Alternate CLI Usage: ./ARodriguez_HW03_happy_primes.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/3Asu9x6mCC0
#
# Description:
# A program to calculate whether a user given number is either of the 
# following types of numbers:
#   - happy prime number
#   - happy non-prime
#   - sad prime number
#   - sad non-prime

# LIBRARIES

# FUNCTIONS
def squared_digit(n):
    """Function to calculate the sum of the squared digits

    Args:
        n (int): an integer which will be split into its digits 

    Returns:
        result (int): an integer representing the sum of squared digits
    """
    if n < 99:
        result = (n % 10)**2 + (n // 10)**2 
        print(f"{n // 10}^2 + {n % 10}^2 = {result}")
    else:
        calc = ""
        for digit in str(n):
            total = 0
            total = total + (int(digit))**2
            calc += f"{digit}^2 + "

        result = total + 1

        #result = f"{''.join(calc)[:-3]} = {result}"
        print(f"{''.join(calc)[:-3]} = {result}")

    return result

def is_happy(n):
    """Function to check if parameter 'n' is a happy number

    Args:
        n (int): an integer that will be checked if it is a happy number

    Returns:
        is_happy (bool): boolean value indicating whether 'integer' is a happy number
    """
    while n != 1:
        is_happy = False

        n = squared_digit(n)

        if n == 1:
            is_happy = True
            break

    return is_happy

def is_prime(n):
    """Function to check if parameter 'n' is a prime number

    Args:
        n (int): an integer that will be checked if it is a prime number

    Returns:
        prime (bool): boolean value indicating whether 'n' is a prime number
    """
    prime = True

    if n < 2:
        prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                prime = False

    return prime

# MAIN PROGRAM FUNCTION
def main():
    
    while True:
        try:
            # Ask end-user to enter a positive number
            integer = int(input(f"Enter a positive integer: "))

            # invoke function to check if number is a happy number
            happy = is_happy(integer)
            
            # invoke function to check if number is a prime number
            prime = is_prime(integer)

            # prints message depending on the result of the boolean expressions
            if happy and prime:
                print(f"The number {integer} is a happy prime number")
                continue

            if happy and not prime:
                print(f"The number {integer} is a happy non-prime number")
                continue

            if not happy and prime:
                print(f"The number {integer} is a sad prime number")
                break

            if not happy and not prime:
                print(f"The number {integer} is a sad non-prime number")
                break

        except KeyboardInterrupt:
            print(f"")
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()
