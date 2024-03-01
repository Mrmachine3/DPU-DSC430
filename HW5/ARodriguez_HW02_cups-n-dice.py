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
# Video Explanation URL: https://youtu.be/TWdLSKfykkY
#
# Description:
# This Python program simulates a dice game where players roll various types of
# dice to match a randomly generated goal number. The code features classes for
# each type of die encapsulating methods for rolling and displaying die values.
# A "Cup" class aggregates the dice and the game logic includes functions for
# betting, balance management, and payout calculations


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
    """A function to print a message to end user that they are exiting the game
        The function also prints the objective of the game

    Args:
        name (str): a variable storing the name of the end user
    """
    # Display a game exit message to user
    print(f"Thanks for playing {name}!\nGoodbye!\n")
    sys.exit()
    
def initialize_game(name,bal):
    """A function to ask the end user if they want to play the game

    Args:
        name (str): a variable storing the name of the end user
        bal (int): a variable storing the initial balance given to the end user

    Returns:
        bal: the available balance for an end user derived from the
        display_balance() function
    """
    # Initialize a control variable for looping structure
    started = False
    # Record response to initiate the game sequence
    response = input("Would you like to play a game? [Y/N] ").lower()

    # Conditional logic to recursively call the play_game() if game has not started yet
    if response[0] == "y" and started == False:
        play_game(response,name,bal=bal)
        print(f"\nOBJECTIVE: Roll dice for a sum as close to the goal\n")
        print(f"\n{name} here's ${bal} for you to play...")
        started = True
    else:
        started = False

    # Display the user's playing balance
    return display_balance(name,bal), started, response
    
def display_balance(name,bal,payout=0):
    """A function for displaying the current balance of the end user

    Args:
        name (str): a variable storing the name of the end user
        bal (int): a variable storing the initial balance given to the end user
        payout (int, optional): a variable storing the total calculated payout
        the end user is eligible to receive based on their betting outcome. Defaults to 0.

    Returns:
        int: a variable storing the end user's available balance
    """
    # Calculate new balance based on the payout
    bal += payout
    # Display the updated balance
    print(f"{name}'s current balance: ${bal}\n")
    return bal
    
def calculate_payout(bet,multiplier):
    """A function to calculate the end user's payout based on their bet, and their earned multiplier

    Args:
        bet (int): the sum of money an end user risk playing the game each round
        multiplier (int): a factor by which the winnings are multiplied by to
        yield a total payout

    Returns:
        int: the total sum earned by the end user derived from the original bet
        amount and the multiplier derived from how close the sum of dice reached the goal number
    """
    # Print out the total payout derived from the initial bet and the earned multiplier
    print(f"Payout: {multiplier} x ${bet} = ${multiplier*bet}")
    return multiplier*bet

def set_multiplier(result,bet,cup,multiplier=0):
    """A function to set the different multipliers necessary to calculate the payouts

    Args:
        result (int): this variable represents the total sum of the face values of each die
        bet (int): the sum of money an end user risk playing the game each round
        cup (obj): an object containing n number of dice of different dice type
        multiplier (int): a factor by which the winnings are multiplied by to
        yield a total payout

    Returns:
        int: an integer representing a total payout the end user earned
    """
    # Set the mulitplier for calculating the payout
    multiplier = multiplier 
    # Print the total sum of rolled dice
    print(f"\n{cup}\nSum of dice: {result}\n")
    return calculate_payout(bet,multiplier)
    
def play_game(init_response,name,bal):
    """A function to carry out the flow of the dice rollign game including the
        betting structure, balance adjustments, and the payout calculations

    Args:
        init_response (str): the response returned from initialize_game()
        name (str): a variable storing the name of the end user
        bal (int): a variable storing the initial balance given to the end user
    """
    # Record the initial response
    response = init_response

    # Generate a random goal upon initiating the game
    if response[0] == "y":
        goal = random.randint(1,100)
        print(f"\nGOAL NUMBER: {goal}")

        # Display user's balance
        bal = display_balance(name,bal)

        # Prompt a user to place a bet
        bet = abs(int(input("How much would you like to bet? ")))

        # Display error when user bets high than available balance or when bets equal zero
        if bet > bal or bal < 0 or bal == 0:
            print(f"{name}, you do not have enough funds to place your bet\n") 
            exit_game(name)

        # Calculate the total balance minus the user's bet
        elif bet <= bal and bal >= 0:
            print(f"\nPlacing bet of ${bet}")
            bal -= bet

            current_bal = display_balance(name,bal)

            # Prompt user to select number of each type of die to place in the cup
            qty_6 = int(input("How many 6-sided dice would you like to roll? "))
            qty_10 = int(input("How many 10-sided dice would you like to roll? "))
            qty_20 = int(input("How many 20-sided dice would you like to roll? "))

            # Create a cup object
            cup = Cup(qty_6,qty_10,qty_20)
            # Roll the dice in the cup
            cup.roll()
            # Add all face values of dice in cup
            result = cup.getSum()

            # Compare sum of dice face values equal to goal
            if result == goal:
                payout = set_multiplier(result,bet,cup,10)
                play_game(response,name,display_balance(name,current_bal,payout))

            # Compare sum of dice face values equal to goal within 3 numbers
            elif result >= (goal - 3) and result <= goal:
                payout = set_multiplier(result,bet,cup,5)
                play_game(response,name,display_balance(name,current_bal,payout))

            # Compare sum of dice face values equal to goal within 10 numbers
            elif result >= (goal - 10) and result <= goal:
                payout = set_multiplier(result,bet,cup,2)
                play_game(response,name,display_balance(name,current_bal,payout))

            # Compare sum of dice face values equal to goal with a multiplier of 0
            else:
                payout = set_multiplier(result,bet,cup)
                play_game(response,name,display_balance(name,current_bal,payout))
        else:
            # Continue playing game if no other previous condition is met
            play_game(response,name,display_balance(name,current_bal,payout))

    else:
        # Exit game if user does not want to play game
        exit_game(name)
        sys.exit()

# MAIN PROGRAM FUNCTION
def main():
    # Prompt the user for their name
    name = input("Hello, what is your name? ").capitalize()
    # Greet the user by their name
    print(f"Greetings {name}!")

    # Initialize game by providing user with $100
    current_bal, started, response = initialize_game(name,int(100))

    while started:
        try:
            # Continuously loop through game play while game flow has started
            play_game(response,name,bal=current_bal)
        except KeyboardInterrupt:
            # Exit game if keyboard interruption is entered
            exit_game(name)
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()