#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/19/2024
# Usage: /usr/bin/python3 ARodriguez_HW10_planet.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW10_planet
# Alternate CLI Usage: ./ARodriguez_HW10_planet.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/RFBWpveA-00
#
# Description:
# This Python program calculates the positions of planets in their orbits and
# determines the distance between them on any given day.

# LIBRARIES
import math

# CLASSES
class Planet():
    """An object that instantiates a Planet object with a radius and the length
        of the planet's year (in days)
    """
    def __init__(self,radius, year):
        """A method to initialize the Planet object with a radius and year

        Args:
            radius (int): length of the planet's radius beginning
                            from origin point to outermost perimeter
            year (int): the number of days required to orbit the sun
        """
        self.radius = radius
        self.year = year

    def position(self, day):
        """A method to calculate the coordinates of a point on the
            outermost perimeter of planet

        Args:
            x (int): x coordinate of point on perimeter
            y (int): y coordinate of point on perimeter

        """
        # Calculate the angle in radians as a proportion of days of a year
        radians = math.radians(day/self.year)*360
        
        # Derive the x coordinate with trigonometric function of cosine
        x = math.cos(radians) * self.radius
        # Derive the y coordinate with trigonometric function of sine
        y = math.sin(radians) * self.radius

        return round(x,2),round(y,2)
    
        
# FUNCTIONS
def test_mercury():
    """Function to initialize the planet mercury and the
        coordinates for points along the perimeter
    """
    mercury = Planet(3.5,88)
    
    days = [0,22,33,440]

    # Display coordinates for each day along mercury's perimeter
    if DEBUG == True:
        for day in days:
            print(f"Day {day}: {mercury.position(day)}\n")

def big_bang():
    """Function to initialize the all the planets of the solar system
        with their respective radii
    """
    data = {
        "Mercury": (3.5, 88),
        "Venus": (6.7, 225),
        "Earth": (9.3, 365),
        "Mars": (14.2, 687),
        "Jupiter": (48.4, 4333),
        "Saturn": (88.9, 10759),
        "Uranus": (179, 30687),
        "Neptune": (288, 60190)
    }
    
    # Initialize empty list to store planet objects
    planets = []

    # Iterating over solar system dictionary to access tuple values necessary to initialize planets
    for name, (radius, year) in data.items():
        if DEBUG == True:
            print(f"Creating {name}: \n  {name.lower()} = Planet({radius}, {year})")

        planet = Planet(radius, year)
        planets.append(planet)
    
    return planets

def distance(planet1, planet2, day):
    """Function to measure distance between two points on perimeter of two distinct planets

    Args:
        planet1 (obj): first Planet object
        planet2 (obj): second Planet object
        day (int): the day on each planet from where to measure distance between both planets

    Returns:
        str: number of miles between one point along the perimeter of two different planets
    """
    # Unpack x and y coordinates of planets 1 & 2
    x1,y1 = planet1.position(day)
    x2,y2 = planet2.position(day)

    # Utilize the pythagorean theorem to calculate the length of the hypotenuse
    distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
    
    return distance

# MAIN PROGRAM FUNCTION
def main():
    # Invoke function to create planet mercury
    test_mercury()

    # Invoke function to create all planets
    planets = big_bang()

    earth = None
    mars = None

    # Iterate through list of planets to assign correct planet objects, identified by planet radii, to variables
    for planet in planets:
        if isinstance(planet, Planet) and planet.radius == 9.3:
            earth = planet
        elif isinstance(planet, Planet) and planet.radius == 14.2:
            mars = planet

    # Validates planet objects exist
    if earth and mars:
        # Invoke function to calculate distance
        d = distance(earth,mars, 732)
        print(f"Distance between Earth and Mars:\n{d:.2f} million miles")

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    DEBUG = False
    main()