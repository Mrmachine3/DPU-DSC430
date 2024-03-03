#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/29/2024
# Usage: /usr/bin/python3 ARodriguez_HW07_war_and_randomness.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW07_war_and_randomness
# Alternate CLI Usage: ./ARodriguez_HW07_war_and_randomness.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/4sVv0JtTauA
#
# Description:
# This program generates pseudo-random numbers using the text of "War and Peace"
# by Leo Tolstoy by extracting all words from the text


# LIBRARIES
import re
import random
from collections import defaultdict

# CLASSES
class WarAndPeacePseudoRandomNumberGenerator():
    """A class that initializes a dictionary of words derived from a corpus
        of text and provides a function for choosing 'n' number of words
        randomly.
    """

    def __init__(self, text):
        """A function to initialize the object containing the word
            frequencies from a corpus using regex

        Args:
            text (str): A corpus of text 
        """
        self.words = re.findall(r'\b\w+\b', text)
        self.word_counts = defaultdict(int)
        for word in self.words:
            self.word_counts[word] += 1
        self.total_words = len(self.words)
        
    def random(self):
        """A function to randomly select a word from a dictionary of
            words and returning the frequency of occurrence

        Returns:
            int: Frequency of word in dictinoary
        """
        random_word = random.choice(self.words)
        return self.word_counts[random_word]
    
    def generate_random_numbers(self, count):
        """ A function for generating a list of random selections

        Args:
            count (int): the number of choices necessary

        Returns:
            list: A list of random numbers
        """
        return [self.random() for _ in range(count)]

    
# MAIN PROGRAM FUNCTION
def main(count):
    text = 'war-and-peace.txt'

    # Read the text version of "War and Peace" and preprocess it
    with open(text, "r", encoding="utf-8") as filename:
        war_and_peace_text = filename.read().lower()
    
    # Create the pseudo-random number generator class
    prng = WarAndPeacePseudoRandomNumberGenerator(war_and_peace_text)
    
    # Generate 10,000 pseudo-random numbers
    r = prng.generate_random_numbers(count)
    print(r)

    # Print the calculated minimum, maximum, and mean of the generated numbers
    print(f"Minimum: {min(r)}\nMaximum: {max(r)}\nMean: {sum(r) / len(r)}")


# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main(4)