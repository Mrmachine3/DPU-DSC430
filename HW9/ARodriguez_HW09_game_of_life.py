#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/14/2024
# Usage: /usr/bin/python3 ARodriguez_HW09_game_of_life.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW09_game_of_life
# Alternate CLI Usage: ./ARodriguez_HW09_game_of_life.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/wuYbHE5e0kY
#
# Description:
# This program implements Conway's Game of Life, which operates on a two-dimensional
# grid of cells, each of which can be in one of two states: alive or dead. The rules
# for evolving the grid from one generation to the next are as follows:

# 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The program initializes a grid of a specified size with a given probability of cells
# being alive at the start. It then simulates the evolution of this grid over a number
# of generations, applying the rules of Conway's Game of Life. At each generation, it
# displays the state of the grid, along with the total population (number of live cells),
# until the population becomes extinct or the specified number of generations is reached.

# LIBRARIES
import numpy as np

# FUNCTIONS
def display(board, pop, gen=0):
    """Function to display the board, current population and the generation

    Args:
        board (matrix): numpy matrix representing all alive/dead cells
        pop (int): total number of alive cells
        gen (int, optional): Each iteration of the game of life. Defaults to 0.
    """
    if pop > 0:
        print(f"\nGeneration {gen}\nPopulation: {pop}\n\n{board}\n")
    else:
        print(f"\nBy the end of generation {gen-1} the entire population perished\n")
        

def conway(size, prob):
    """Function to initialize the board at generation 0

    Args:
        size (int): dimension for square grid
        prob (float): percentage of alive cells

    Returns:
        nparray: generation 0 board
    """
    if size >= 3: 
        # Initialize generation 0 of board
        alive_cells = int(size * size * prob)
        board = np.zeros((size, size), dtype=int)
        indices = np.random.choice(size*size, alive_cells, replace=False)
        board.flat[indices] = 1

        # Display state of cells if DEBUG is TRUE
        if DEBUG == True:
            for i in range(size):
                for j in range(size):
                    if board[i,j] == 1:
                        print(f"{board[i,j]}: Alive!")
                    else:
                        print(f"{board[i,j]}: Dead!")

        return board
    else:
        print(f"Board size of {size} is invalid")

def count_population(board):
    """Function to sum all alive cells on the board

    Args:
        board (nparray): represents an game of life and alive/dead cells

    Returns:
        int: total of alive cells
    """
    return np.sum(board)

def count_living(board,i,j):
    """Function to count all alive cells in an array

    Args:
        board (nparray): represents an game of life and alive/dead cells
        i: iterable for the row in the nparray
        j: iterable for the column in the nparray

    Returns:
        int: total count of live cells
    """
    # Coordinates for all neighbors
    neighbor_coords = [
        (-1,-1), # Above left neighbor
        (-1,0), # Above center neighbor
        (-1,1), # Above right neighbor
        (0,-1), # Left neighbor
        (0,1), # Right neighbor
        (1,-1), # Below left neighbor
        (1,0), # Below center neighbor
        (1,1) # Below right neighbor
    ]

    alive_neighbors = 0

    # Iterate through all neighbors to check on state
    for nrow, ncol in neighbor_coords:
        ni, nj = i + nrow, j + ncol
        
        if 0 <= ni < board.shape[0] and 0 <= nj < board.shape[1]:
            alive_neighbors += board[ni,nj]
    
    return alive_neighbors

def advance(board,generation):
    """Function to proceed to next iteration of generation in game of life

    Args:
        board (nparray): represents an game of life and alive/dead cells
        generation (int): value representing current period of game of life
    """
    # Iterate through range of generations
    for n in range(generation):
        # Determine the starting population
        population = count_population(board)
        if population == 0:
            break
        
        # Create a new board to populate values with results of life for new generation
        new_board = np.copy(board)
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                alive_neighboars = count_living(board, i, j)
                if board[i, j] == 1:
                    if alive_neighboars < 2 or alive_neighboars > 3:
                        new_board[i, j] = 0
                    else:
                        if alive_neighboars == 3:
                            new_board[i, j] = 1

        board = new_board
        display(board, count_population(board), n+1)

# MAIN PROGRAM FUNCTION
def main():
    try:
        # Seek input from user
        size = int(input('Enter grid size: '))
        probability = float(input('Enter probability percentage (decimal): '))
        generations = int(input('Enter simulated generations: '))

        # initialize first generation
        board = conway(size, probability)
        display(board, count_population(board))

        # Advance to next generations
        advance(board,generations)

    except ValueError as e:
        print("Displaying board with test values:")
        size = 3
        probability = 0.5
        generations = 3

        board = conway(size, probability)
        display(board)

        advance(board,generations)


if __name__ == "__main__":
    global DEBUG
    DEBUG = False
    main()