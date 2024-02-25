#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/19/2024
# Usage: /usr/bin/python3 ARodriguez_HW06_palindrome_dates.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW06_palindrome_dates
# Alternate CLI Usage: ./ARodriguez_HW06_palindrome_dates.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES

# FUNCTIONS
def is_palindrome_date(date):
    """A function to check if a date is a palindrome

    Args:
        date (str): a string representation of a date in MM/DD/YYYY

    Returns:
        bool: True if MM/DD/YYYY is equal to YYYY/MM/DD
    """
    return date == date[::-1]

def generate_dates():
    """A function to generate all dates in the 21st century

    Returns:
        list: a list of all dates in the 21st century in MM/DD/YYYY format
    """
    dates = []
    for year in range(2001, 2101):
        for month in range(1, 13):
            for day in range(1, 32):
                dates.append(f"{day:02d}{month:02d}{year}")
    return dates

def check_dates():
    palindrome_dates = []
    all_dates = generate_dates()
    #print(all_dates)

    for date in all_dates:
        if is_palindrome_date(date):
            palindrome_dates.append(date)
    return palindrome_dates

def save_palindrome_dates(filename):
    """A function to save data to a file

    Args:
        filename: output file to save data
    """
    with open(filename, 'w') as file:
        for date in check_dates():
            date = f"{date[0:2]}/{date[2:4]}/{date[4:]}"
            print(f"{date}")
            file.write(date + '\n')

# MAIN PROGRAM FUNCTION
def main():
    """The main function that invokes the function to save a file
    """
    output_file = "palindrome_dates.txt"
    save_palindrome_dates(output_file)
    print(f"Confirmed palindrome dates saved\nFilename: {output_file}")

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()
