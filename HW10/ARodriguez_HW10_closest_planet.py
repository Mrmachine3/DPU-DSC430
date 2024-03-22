#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/19/2024
# Usage: /usr/bin/python3 ARodriguez_HW10_closest_planet.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW10_closest_planet
# Alternate CLI Usage: ./ARodriguez_HW10_closest_planet.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CLASSES
class Planet():
    """An object that instantiates a Planet object with a radius and the length
        of the planet's year (in days)
    """
    def __init__(self,name,radius, year):
        """A method to initialize the Planet object with a radius and year

        Args:
            name (str): name of the planet
            radius (int): length of the planet's radius beginning
                            from origin point to outermost perimeter
            year (int): the number of days required to orbit the sun
        """
        self.name = name
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
    
def distance(planet1, planet2, day):
    """Function to measure distance between two points on perimeter of two distinct planets

    Args:
        planet1 (obj): first Planet object
        planet2 (obj): second Planet object
        day (int): the day on each planet from where to measure distance between both planets

    Returns:
        int: number of miles between one point along the perimeter of two different planets
    """
    # Unpack x and y coordinates of planets 1 & 2
    x1,y1 = planet1.position(day)
    x2,y2 = planet2.position(day)

    # Utilize the pythagorean theorem to calculate the length of the hypotenuse
    return math.sqrt((x2 - x1)**2 + (y2 -y1)**2)

def simulate_time(planets, sim_duration):
    """Function to measure distances between planets over n duration

    Args:
        planets (obj): a planet object defining the name, radius, and orbital year
        sim_duration (int): interval of time representing the simulation duration in days

    Returns:
        int: calculated average distance over the simulation duration
    """
    # Initialize variables at zero to incrementally increase after iteration calculations
    total_distance = 0
    total_pairs = 0

    # Iterate over the total days in the simulation
    for day in range(sim_duration):
        # Initialize variables at zero to incrementally increase after daily calculations
        daily_distance = 0
        daily_pairs = 0

        # Iterate over all planets to identify the 1st planet needed for the distance calculation
        for i in range(len(planets)):
            # Iterate over all planets to identify the 2nd planet needed for the distance calculation
            for j in range(i+1, len(planets)):
                # Call distance function and passing in parameters
                d = distance(planets[i], planets[j], day)
                daily_distance += d
                daily_pairs += 1

        # Calculate average daily distances amongst all planet pairs
        avg_daily_distance = daily_distance / daily_pairs
        total_distance += avg_daily_distance
        total_pairs += 1
        
    # Calculate average total distances amongst all planet pairs
    return round((total_distance / total_pairs), 2)

def display_grid(planets, distances):
    """_summary_

    Args:
        planets (list): a list of all instances of planets in solar system
        distances (np.ndarray): an 8x8 matrix of calculated distances between planet pairs

    Returns:
        distances (np.ndarray): an 8x8 matrix of calculated distances between planet pairs
    """
    # Display the distance grid with planet names as row/column headings
    grid = ""
    grid += "Average Distance between each pair of planets:\n"
    headers = "\t".join([planet.name for planet in planets])
    grid += f"\t{headers}"
    for i, row in enumerate(distances):
        grid += f"\n{planets[i].name}\t"
        for distance_val in row:
            grid += f"{distance_val:.2f}\t"

    # A labeled grid with planet names and updated distance values
    return grid

def write_distances_to_file(earth, other_planets, sim_days, sim_years, filename):
    """Function to write the distances of selected planets to a file

    Args:
        earth (obj): an instance of the planet earth
        other_planets (list): a list containing instances of mercury, venus, and mars
        sim_days (int): a number of days representing an orbital year
        sim_years (int): a number of orbital years
        filename (str): the name of the desired output file
    """
    # file context manager to write the distances between planets to rows
    with open(filename, 'w') as file:
        file.write("Mercury,Venus,Mars\n")
        for day in range(sim_days * sim_years):
            mercury_distance = distance(earth, other_planets[0], day)
            venus_distance = distance(earth, other_planets[1], day)
            mars_distance = distance(earth, other_planets[2], day)
            file.write(f"{mercury_distance:.2f},{venus_distance:.2f},{mars_distance:.2f}\n")

def generate_dataset(planets, filename, sim_days=1000, sim_years=1):
    """Function to generate the distances data set for selected planets

    Args:
        planets (list): a list containing instances of all planets
        sim_days (int, optional): a number of days representing an orbital year
        sim_years (int, optional): a number of orbital years
        filename (str): the name of the desired output file
    """
    # Defining variables for select planets
    earth = planets[2]
    other_planets = [planets[0], planets[1], planets[3]]

    # Call function to write distance data to a file
    write_distances_to_file(earth, other_planets, sim_days, sim_years, filename)

def plot_timeseries(filename):
    """Function to plot dataset from input file

    Args:
        filename (str): the name of the desired output file
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)
    df.index = np.arange(1, len(df) +1)
    df['Day'] = df.index

    figtxt = f"Simulation interval: {len(df.index)} days"

    # Plot the time series graph with labels and legend
    plt.figure(figsize=(10, 6))
    plt.plot(df['Day'], df['Mercury'], label='Mercury')
    plt.plot(df['Day'], df['Venus'], label='Venus')
    plt.plot(df['Day'], df['Mars'], label='Mars')
    plt.xlabel('Day')
    plt.ylabel('Distance')
    plt.title('Distance from Earth to Other Planets Over Time')
    plt.legend()
    plt.figtext(0,0,figtxt)
    plt.grid(True)
    plt.show()


# MAIN PROGRAM FUNCTION
def main(sim_days, sim_years, filename):
    # Solar system dictionary of tuple values containing radii and orbital years
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

    # Initialize list of planet objects
    planets = [Planet(name,radius, year) for name, (radius, year) in data.items()]

    # Initializes matrix of zeros 
    distances = np.zeros((len(planets), len(planets)))

    # Iterate over list of planet pairs to update matrix with average distances
    for i in range(len(planets)):
        for j in range(i, len(planets)):
            avg_distance = simulate_time([planets[i],planets[j]], (sim_days * sim_years))
            distances[i][j] = avg_distance
            distances[j][i] = avg_distance

    # Printing grid results from 'display_grid' function call
    print(display_grid(planets, distances))

    # Calling function to generate data set
    generate_dataset(planets, filename)

    # Calling function to plot timeseries data from previously generated data set
    plot_timeseries(filename)

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    np.set_printoptions(precision=2)

    sim_years = 1000
    sim_days = 365
    filename = "earth_distances.csv"

    main(sim_days, sim_years, filename)