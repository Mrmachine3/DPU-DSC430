#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 01/23/2024
# Path: /mnt/c/Users/atone/Desktop/DPU-DSC430/ARodriguez_HW02stem_n_leaf.py
# Usage: /usr/bin/python3 ARodriguez_HW02stem_n_leaf.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW02stem_n_leaf
# Alternate CLI Usage: ./ARodriguez_HW02stem_n_leaf.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:
# This program reads the contents of a file containing numbers on each line and
# parses the data to produce a stem and leaf plot to illustrate the
# distribution of the data stored in the file.

# LIBRARIES
import sys

# FUNCTIONS
def compute_stemleaves(data):
    """Function returns the compiled output representing a stem and leaf graph

    Args:
        data (list): A list of numbers compiled by the read_file() function

    Returns:
        d (list): A list of stems and leaves derived from the list of numbers
        passed into the function
    """
    # Initialize an empty list
    d = []

    # The position at which to split leaves from stems, i.e. tens place
    interval = 10

    # Loop through the sorted list of data to calculate the stem and leaf pairs
    # Division operation calculated on integers where the result is cast to
    # strings, split by ".", and appended to 'd' as a pair of integers
    # representing the stem and leaf
    for data in sorted(data):
        stm, lf = str((data/interval)).split(".")
        d.append((int(stm), int(lf)))

    return d

def plot_stem(filename,d):
    """Function returns the compiled output representing a stem and leaf graph

    Args:
        filename (str): The filename selected from the read_option() function
        d (list): A list of stems and leaves derived from the list of numbers

    Returns:
        (str): A string representation of the list of stems and leaves derived
        from the list of numbers passed into the function
    """
    # Unpacking a list of tuples representing the stem and leaf components of the initial dataset
    stems, leafs = list(zip(*d))
    

    # Calculating the max widths for the stems and leafs to prepare for outputing the chart
    stmwidth = max(len(str(x)) for x in  stems)
    lfwidth = max(len(str(x)) for x in leafs)
    laststem = min(stems) - 1
    
    # Initialize empty list for output
    out = []

    # Iterate over stem and leaf tuples to calculate the length to determine proper spacing in plot
    for s, l in d:
        if len(str(s)) == 1:
            space = f"{'  '}"
        elif len(str(s)) == 2:
            space = f"{' '}"
        else:
            space = f"{''}"

        while laststem < s:
            laststem += 1
            out.append(f"\n{space}{int(s)} |")
        out.append(f" {int(l)}")

    # output list of strings joined without whitespacing or new lines
    return "".join(out)


def read_file(filename):
    """Function to open each file in a context manager to read dataset into memory

    Args:
        filename (str): The filename selected from the read_option() function

     Returns:
        data (list): A list of numbers stripped of newlines and trailing whitespace
    """
    # Open file in context manager in read-mode
    with open(filename, 'r') as raw:
        # In a list comprehension, iterate through lines in context called raw
        # strip all whitespace and convert to integer
        data = [int(line.rstrip()) for line in raw]
    
    return data


def read_option(selection):
    """Function to store end-user option selection indicating which file to process

    Args:
        selection (str): A string representing a menu selection

     Returns:
        filename (str): A string representing the name of the file listed in menu options
    """
    # If-else condition to assign selected file to process to filename variable
    # End-user may also enter exit or press Ctrl + C to exit program
    if selection == "1":
        filename = "StemAndLeaf1.txt"
    elif selection == "2":
        filename = "StemAndLeaf2.txt"
    elif selection == "3":
        filename = "StemAndLeaf3.txt"
    elif selection.lower() == "exit":
        print(f"Exiting...")
        sys.exit()
    else:
        pass

    return filename


# MAIN PROGRAM FUNCTION
def main():
    """Function call to invoke a while True loop to welcome user and prompt for a selection

    Returns:
        plot (str): A rendered graphical representation of the stems and leaves
        derived from the filename dataset
    """
    # Start a while true loop to continuously prompt user for option selection
    while True:
        try:
            print(f"\nWelcome to the stem and leaf chart plotter tool!")
            print(f"  1 - StemAndLeaf1.txt")
            print(f"  2 - StemAndLeaf2.txt")
            print(f"  3 - StemAndLeaf3.txt")
            print(f"  Exit/Ctrl + C - Exit program")
        
            selection = str(input(f"\nEnter option as 1, 2, 3, or exit to quit: "))

            # Invoke read_option() with selection as parameter to extract filename
            filename = read_option(selection)

            # Invoke read_file() with filename variable as parameter to read dataset into memory
            data = read_file(filename)

            # Invoke compute_stemleaves() with data variable to compute stem/leaves
            stemleaves = compute_stemleaves(data)

            # Invoke plot_stem() with stems/leaves to compile chart
            plot = plot_stem(filename,stemleaves)

            # Print message indicating what file is being processed
            print(f"\nCharting data from {filename}\n{plot}\n{('~'*80)}")

        except UnboundLocalError:
            print(f"Unrecognized option. Try again")
            continue
        except KeyboardInterrupt:
            print(f"\nExiting...")
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()
