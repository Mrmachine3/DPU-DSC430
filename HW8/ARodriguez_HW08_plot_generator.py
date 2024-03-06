#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/05/2024
# Usage: /usr/bin/python3 ARodriguez_HW08_plot_generator.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW08_plot_generator
# Alternate CLI Usage: ./ARodriguez_HW08_plot_generator.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
import os
import random

# CLASSES
class SimplePlotGenerator:
    """A class for generating simple plot"""

    def generate(self):
        """Function to generate a simple plot description"""
        return f"\tSomething happens"


class RandomPlotGenerator(SimplePlotGenerator):
    """A class for generating a random plot based on reference text"""

    def generate(self):
        """Function to randomly select plot elements from reference text"""
        name = pv.random_choice('plot_names.txt')
        adj = pv.random_choice('plot_adjectives.txt')
        profession = pv.random_choice('plot_professions.txt')
        verb = pv.random_choice('plot_verbs.txt')
        evil_adj = pv.random_choice('plot_adjectives_evil.txt')
        villain_job = pv.random_choice('plot_villian_job.txt')
        villain = pv.random_choice('plot_villains.txt')
        
        return f"\t{name[0]}, a {adj[0]} {profession[0]}, must {verb[0]} the {evil_adj[0]} {villain_job[0]}, {villain[0]}."


class InteractivePlotGenerator(SimplePlotGenerator):
    """A class for generating a random plot based on reference text yet offers interaction to user"""

    def generate(self):
        """Function to randomly select five of each plot element from reference text"""
        choices = []
        plot_names_list = [pv.random_choice('plot_names.txt') for _ in range(5)]
        plot_adjectives_list = [pv.random_choice('plot_adjectives.txt') for _ in range(5)]
        plot_professions_list = [pv.random_choice('plot_professions.txt') for _ in range(5)]
        plot_verbs_list = [pv.random_choice('plot_verbs.txt') for _ in range(5)]
        plot_evil_adj_list = [pv.random_choice('plot_adjectives_evil.txt') for _ in range(5)]
        plot_villain_job_list = [pv.random_choice('plot_villian_job.txt') for _ in range(5)]
        plot_villains_list = [pv.random_choice('plot_villains.txt') for _ in range(5)]

        [print(str(i[0]), end='\n') for i in plot_names_list]
        selection = pv.queryUser(f"\nSelect protagonist's name for plot generation: ")
        choices.append(plot_names_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_adjectives_list]
        selection = pv.queryUser(f"\nSelect adjective for plot generation: ")
        choices.append(plot_adjectives_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_professions_list]
        selection = pv.queryUser(f"\nSelect protagonist's profession for plot generation: ")
        choices.append(plot_professions_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_verbs_list]
        selection = pv.queryUser(f"\nSelect verb for plot generation: ")
        choices.append(plot_verbs_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_evil_adj_list]
        selection = pv.queryUser(f"\nSelect evil adjective for plot generation: ")
        choices.append(plot_evil_adj_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_villain_job_list]
        selection = pv.queryUser(f"\nSelect antagonist's job for plot generation: ")
        choices.append(plot_villain_job_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_villains_list]
        selection = pv.queryUser(f"\nSelect antagonist's name for plot generation: ")
        choices.append(plot_villains_list[int(selection)-1][0])

        return f"\n\t{choices[0]}, a {choices[1]} {choices[2]}, must {choices[3]} the {choices[4]} {choices[5]}, {choices[6]}."

class PlotViewer:
    """
    A class representing the viewer of plot generators.

    This class allows registration of different plot generator instances and facilitates generating plots
    using methods to ask for user input and to randomly make a selection.
    """
    def registerPlotGenerator(self, pg):
        """Function to register a generator and abstract away methods to view the data"""
        self.pg = pg
        self.pg.registerPlotGenerator(self)

    def queryUser(self, str):
        """Function to query a user for input"""
        return input(str)

    def random_choice(self, filename):
        """Function to facilitate the random selection of plot elements"""
        choices = []
        with open(filename, 'r') as fin:
            data = [line.rstrip() for line in fin.readlines()]
            choices.append(random.choice(data))
        return choices

# MAIN PROGRAM FUNCTION
# Instantiate an object of the PlotViewer() class
pv = PlotViewer()

# Instantiate objects of the different plot generator classes
sg = SimplePlotGenerator()
pg = RandomPlotGenerator()
ig = InteractivePlotGenerator()

# Processes invoking the plot generation function for each object defined
print("Attempting: SimplePlotGenerator")
print(f"{sg.generate()}\n")

print("Attempting: RandomPlotGenerator")
print(f"{pg.generate()}\n")

print("Attempting: InteractivePlotGenerator\n")
print(f"{ig.generate()}\n")