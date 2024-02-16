#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/13/2024
# Usage: /usr/bin/python3 ARodriguez_HW01_dice-n-cups.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW01_dice-n-cups
# Alternate CLI Usage: ./ARodriguez_HW01_dice-n-cups.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/f5bCLkVPMDg
#
# Description:
# This program implements the SixSidedDie, TenSidedDie, TwentySidedDie, and Cup
# classes to provide the methods for rolling and retrieving the values of each
# individual die in the cup and also the ability to compute the sum of all
# values.

# LIBRARIES
import random

# CLASSES
class SixSidedDie():
    """Implementation of class type SixSided Die with various methods"""

    def __init__(self):
        """Initialization of class variable for number of sides to the die"""
        self.sides = 6
        
    def roll(self):
        """Method to roll the die"""
        self.value = random.randint(1, self.sides)
        return self.value

    def getFaceValue(self):
        """Method to view the value of the die"""
        if self.value is not None:
            return self.value

    def __repr__(self):
        """Method to display the canonical string version of class variables"""
        return f"SixSidedDie({self.value})"
    
class TenSidedDie(SixSidedDie):
    """Implementation of class type TenSided Die with various methods"""

    def __init__(self):
        """Initialization of class variable for number of sides to the die"""
        self.sides = 10

    def __repr__(self):
        """Method to display the canonical string version of class variables"""
        return f"TenSidedDie({self.value})"
        
class TwentySidedDie(SixSidedDie):
    """Implementation of class type TwentySided Die with various methods"""

    def __init__(self):
        """Initialization of class variable for number of sides to the die"""
        self.sides = 20
        
    def __repr__(self):
        """Method to display the canonical string version of class variables"""
        return f"TwentySidedDie({self.value})"
        
class Cup(TwentySidedDie,TenSidedDie,SixSidedDie):
    """Implementation of class type Cup with inherited object classes for various die"""

    def __init__(self, qty_6=1, qty_10=1, qty_20=1):
        """Initialization of class variables for number die placed inside of cup"""
        self.dice = []
        self.qty_6 = qty_6
        self.qty_10 = qty_10
        self.qty_20 = qty_20
        self.sum = 0

        for _ in range(qty_6):
            self.dice.append(SixSidedDie())    
        for _ in range(qty_10):
            self.dice.append(TenSidedDie())    
        for _ in range(qty_20):
            self.dice.append(TwentySidedDie())    

    def roll(self):
        """Method to roll the dice in the cup"""
        self.sum = 0
        for die in self.dice:
            self.sum += die.roll()
        return self.sum
    
    def getSum(self):
        """Method to add get all face values of dice and add them for a total number"""
        return self.sum
    
    def __repr__(self):
        """Method to display the canonical string version of class variables"""
        return f"Cup({','.join([str(i) for i in self.dice])})"

# MAIN PROGRAM FUNCTION
def main():
    print(f"Rolling a single 6-sided die:")
    six = SixSidedDie()
    print(six.roll())
    print(six.getFaceValue())
    print(six)

    print("")
    print(f"Rolling a cup of dice:")
    cup = Cup(1,2,1)
    print(cup.roll())
    print(cup.getSum())
    print(cup)

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()
