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
        radians = math.radians(day/self.year)*360
        
        x = math.cos(radians) * self.radius
        y = math.sin(radians) * self.radius

        return round(x,2),round(y,2)
    
        
# FUNCTIONS
def test_mercury():
    mercury = Planet(3.5,88)
    
    days = [0,22,33,440]

    if DEBUG == True:
        for day in days:
            print(f"Day {day}: {mercury.position(day)}\n")

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

    for name, (radius, year) in data.items():
        if DEBUG == True:
            print(f"Creating {name}: \n  {name.lower()} = Planet({radius}, {year})")

        planet = Planet(radius, year)
        planets.append(planet)
    
    return planets

def distance(planet1, planet2, day):
    x1,y1 = planet1.position(day)
    x2,y2 = planet2.position(day)

    distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
    
    return distance

# MAIN PROGRAM FUNCTION
def main():
    test_mercury()

    planets = big_bang()

    earth = None
    mars = None

    for planet in planets:
        if isinstance(planet, Planet) and planet.radius == 9.3:
            earth = planet
        elif isinstance(planet, Planet) and planet.radius == 14.2:
            mars = planet

    if earth and mars:
        d = distance(earth,mars, 732)
        print(f"Distance between Earth and Mars:\n{d:.2f}")

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    DEBUG = False
    main()