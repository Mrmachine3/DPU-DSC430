#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/02/2024
# Usage: /usr/bin/python3 ARodriguez_HW07_Overlapping_ellipses.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW07_Overlapping_ellipses
# Alternate CLI Usage: ./ARodriguez_HW07_Overlapping_ellipses.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/h-cfeQKEiQE
# Description:
# A program to calculate the area of overlapping ellipses.


# LIBRARIES
import math
import random
import re
from collections import defaultdict

# CLASSES
class Pseudo_Number_Generator:
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
        random_word = random.choice(range(11))
        return self.word_counts[random_word]
    
    def generate_random_numbers(self, count):
        """ A function for generating a list of random selections

        Args:
            count (int): the number of choices necessary

        Returns:
            list: A list of random numbers
        """
        return [self.random() for _ in range(count)]

    
class Point:
    """Implementation of class type Point with methods"""

    def __init__(self,x, y):
        """Initialization coordinates of point"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Display the canonical string version of class"""
        return f"Point({self.x},{self.y})"


class Ellipse(Point):
    """Implementation of class type Ellipse with methods"""

    def __init__(self, pointA, pointB, maj_axis_diameter):
        """Initialization of point coordinates and width"""
        self.pointA = pointA
        self.pointB = pointB
        self.maj_axis_diameter = maj_axis_diameter

    def computeArea(self):
        """A function to calculate the area of an Ellipse

        Returns:
            float: A computed float value representing the area of an ellipse
        """
        self.a = self.maj_axis_diameter/2
        self.b = math.sqrt((self.pointA.x - self.pointB.x) ** 2 + (self.pointA.y - self.pointB.y) ** 2)/2
        return f"{(math.pi * self.a * self.b):0.4f}"
        
    def __repr__(self):
        """Display the canonical string version of class"""
        return f"Ellipse({self.pointA},{self.pointB},{self.maj_axis_diameter})"
    

class Circle(Ellipse):
    """Implementation of class type Ellipse with methods"""
    
    def computeArea(self):
        """A function to calculate the area of an Circle

        Returns:
            float: A computed float value representing the area of an circle
        """
        self.a = self.maj_axis_diameter/2
        return f"{math.pi * (self.a**2):0.4f}"

    def __repr__(self):
        """Display the canonical string version of class"""
        if self.pointA == self.pointB:
            return f"Circle({self.pointA},{self.maj_axis_diameter})"
        else:
            return f"Circle({self.pointA},{self.pointB},{self.maj_axis_diameter})"
    

# FUNCTIONS
def computeOverlapOfEllipses(ellipse1, ellipse2):
    """Function to compute the area of overlap between two intersecting ellipses

    Args:
        ellipse1 (obj): Ellipse 1 object
        ellipse2 (obj): Ellipse 2 object
    """
    # Define the number of divisions for numerical integration
    #divisions = 10000
    divisions = 1000

    # Initialize the area of overlap
    overlap_area = 0

    # Calculate the step size for each dimension
    step_x = (max(ellipse1.pointA.x, ellipse1.pointB.x, ellipse2.pointA.x, ellipse2.pointB.x) -
                min(ellipse1.pointA.x, ellipse1.pointB.x, ellipse2.pointA.x, ellipse2.pointB.x)) / divisions
    step_y = (max(ellipse1.pointA.y, ellipse1.pointB.y, ellipse2.pointA.y, ellipse2.pointB.y) -
                min(ellipse1.pointA.y, ellipse1.pointB.y, ellipse2.pointA.y, ellipse2.pointB.y)) / divisions

    # Iterate through each grid cell and check if it's within both ellipses
    for i in range(divisions):
        for j in range(divisions):
            x = min(ellipse1.pointA.x, ellipse1.pointB.x) + i * step_x
            y = min(ellipse1.pointA.y, ellipse1.pointB.y) + j * step_y
            if is_inside_ellipse(x, y, ellipse1) and is_inside_ellipse(x, y, ellipse2):
                overlap_area += step_x * step_y

    return overlap_area

def is_inside_ellipse(x, y, ellipse):
    """A function to verify of a point is within the area of an ellipse

    Args:
        x (int): The x-value of the coordinate for the point 
        y (int): The y-value of the coordinate for the point 
        ellipse (obj): an Ellipse object with two points at the foci

    Returns:
        bool: A boolean value indicating whether the computed value is less than 1
    """
    try:
        a = ellipse.maj_axis_diameter / 2
        b = math.sqrt((ellipse.pointA.x - ellipse.pointB.x) ** 2 + (ellipse.pointA.y - ellipse.pointB.y) ** 2) / 2
        return ((x - ellipse.pointA.x) ** 2) / (a ** 2) + ((y - ellipse.pointA.y) ** 2) / (b ** 2) <= 1
    except:
        pass

def test_two_circles_at_origin():
    """Test function to calculate the overlapping area between two circles"""
    print(f"Testing two circles at origin point:")
    # Circle A
    width_a = 2
    e1 = Circle(Point(0,0),Point(0,0),width_a)

    # Circle B
    width_b = 4
    e2 = Circle(Point(0,0),Point(0,0),width_b)

    print(f"{e1} has area: {e1.computeArea()}")
    print(f"{e2} has area: {e2.computeArea()}")

    print(f"The area of overlap between both ellipses: {computeOverlapOfEllipses(e1,e2)} ")
    print("")


def test_complex_example():
    """Test function to calculate the overlapping area between two ellipses"""
    print(f"Testing two complex examples:")
    # Ellipse A
    p1 = Point(0,0)
    p2 = Point(4,0)
    width_a = 6
    e1 = Ellipse(p1,p2,width_a)

    # Ellipse B
    p3 = Point(3,3)
    p4 = Point(7,3)
    width_b = 4
    e2 = Ellipse(p3,p4,width_b)

    print(f"{e1} has area: {e1.computeArea()}")
    print(f"{e2} has area: {e2.computeArea()}")

    print(f"The area of overlap between both ellipses: {computeOverlapOfEllipses(e1,e2)} ")
    print("")

def test_multiple_example(num_range):
    """Test function to calculate the overlapping area between various pairs of points"""
    for i in num_range:
        for j in num_range:
            for k in num_range:
                for l in num_range:
                    print(f"Testing points ({i},{j}), ({k},{l}) examples:")
                    # Ellipse A
                    p1 = Point(i,j)
                    p2 = Point(-k,l)
                    width_a = 6
                    e1 = Ellipse(p1,p2,width_a)

                    # Ellipse B
                    p3 = Point(-i,-j)
                    p4 = Point(k,-j)
                    width_b = 4
                    e2 = Ellipse(p3,p4,width_b)

                    print(f"{e1} has area: {e1.computeArea()}")
                    print(f"{e2} has area: {e2.computeArea()}")

                    print(f"The area of overlap between both ellipses: {computeOverlapOfEllipses(e1,e2)} ")
                    print("")

# MAIN PROGRAM FUNCTION
def main(count):
    text = 'war-and-peace.txt'

    # Read the text version of "War and Peace" and preprocess it
    with open(text, "r", encoding="utf-8") as filename:
        war_and_peace_text = filename.read().lower()
    
    # Create the pseudo-random number generator class
    prng = Pseudo_Number_Generator(war_and_peace_text)
    
    # Generate pseudo-random numbers
    r = range(4)
    
    #test_two_circles_at_origin()
    #test_complex_example()
    test_multiple_example(r)

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main(4)
