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
# Video Explanation URL:
#
# Description:


# LIBRARIES
import math

# CLASSES
class Planet():
    def __init__(self,radius, year):
        self.radius = radius
        self.year = year

    def position(self, day):
        """
        to find the length of each leg of a right triangle, divide the hypotenuse by the sqrt of 2
        
        45-45-90 triangle with a hypotenuse of 30
        a = 30/math.sqrt(2)
        b = 30/math.sqrt(2)
        c = 30

        Calculate the angel by finding a fraction equal to the day divided by the value of a full year
        multiply the fraction by 360 degrees to find the angle.

        example:
        day = 22
        year = 88
        
        (22/88) * 360 = 90
        (33/88) * 360 = 135 
        """
        radians = math.radians(((day/self.year)*360))
        
        x = math.cos(radians) * self.radius
        y = math.sin(radians) * self.radius

        return f'{x:.2f}, {y:.2f}'
        
# FUNCTIONS
def test_mercury():
    mercury = Planet(3.5,88)
    
    days = [0,22,33,440]

    for day in days:
        print(f"Day {day}:\n  {mercury.position(day)}\n")

def big_bang():
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
    
    planets = []

    for name, (radius, days) in data.items():
        print(f"Creating {name}: \n  {name.lower()} = Planet({radius}, {days})")
        planet = Planet(radius, days)
        planets.append(planet)
    
    return planets

def distance():
    pass

# MAIN PROGRAM FUNCTION
def main():
    test_mercury()

    big_bang()

    d = distance(earth,mars, 732)

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()