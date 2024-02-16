#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/14/2024
# Usage: /usr/bin/python3 ARodriguez_HW02_cups-n-dice.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW02_cups-n-dice
# Alternate CLI Usage: ./ARodriguez_HW02_cups-n-dice.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
import random
import sys

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
    
# FUNCTIONS
def exit_game(name):
    print(f"Thanks for playing {name}!\nGoodbye!\n")
    sys.exit()
    
def initialize_game(name,bal):
    started = False
    response = input("Would you like to play a game? [Y/N] ").lower()

    if response[0] == "y" and started == False:
        play_game(response,name,bal=bal)
        print(f"\nOBJECTIVE: Roll dice for a sum as close to the goal\n")
        print(f"\n{name} here's ${bal} for you to play...")
        started = True
    else:
        started = False

    return display_balance(name,bal), started, response
    
def display_balance(name,bal,payout=0):
    bal += payout
    print(f"{name}'s current balance: ${bal}\n")
    return bal
    
def calculate_payout(bet,multiplier):
    print(f"Payout: {multiplier} x ${bet} = ${multiplier*bet}")
    return multiplier*bet

def compare_result(result,bet,cup,multiplier=0):
    multiplier = multiplier 
    print(f"\n{cup}\nSum of dice: {result}\n")
    return calculate_payout(bet,multiplier)
    
def play_game(init_response,name,bal):
    response = init_response

    if response[0] == "y":
        goal = random.randint(1,100)
        print(f"\nGOAL NUMBER: {goal}")

        bal = display_balance(name,bal)

        bet = int(input("How much would you like to bet? "))

        if bet > bal or bal < 0 or bal == 0:
            print(f"{name}, you do not have enough funds to place your bet\n") 
            exit_game(name)

        elif bet <= bal and bal >= 0:
            print(f"\nPlacing bet of ${bet}")
            bal -= bet

            current_bal = display_balance(name,bal)

            qty_6 = int(input("How many 6-sided dice would you like to roll? "))
            qty_10 = int(input("How many 10-sided dice would you like to roll? "))
            qty_20 = int(input("How many 20-sided dice would you like to roll? "))

            cup = Cup(qty_6,qty_10,qty_20)
            cup.roll()
            result = cup.getSum()

            if result == goal:
                payout = compare_result(result,bet,cup,10)
                play_game(response,name,display_balance(name,current_bal,payout))

            elif result >= (goal - 3) and result <= goal:
                payout = compare_result(result,bet,cup,5)
                play_game(response,name,display_balance(name,current_bal,payout))

            elif result >= (goal - 10) and result <= goal:
                payout = compare_result(result,bet,cup,2)
                play_game(response,name,display_balance(name,current_bal,payout))

            else:
                payout = compare_result(result,bet,cup)
                play_game(response,name,display_balance(name,current_bal,payout))
        else:
            play_game(response,name,display_balance(name,current_bal,payout))

    else:
        exit_game(name)
        sys.exit()

# MAIN PROGRAM FUNCTION
def main():
    name = input("Hello, what is your name? ").capitalize()
    print(f"Greetings {name}!")

    current_bal, started, response = initialize_game(name,int(100))

    while started:
        try:
            play_game(response,name,bal=current_bal)
        except KeyboardInterrupt:
            exit_game(name)
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()