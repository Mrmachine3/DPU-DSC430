#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 03/05/2024
# Usage: /usr/bin/python3 ARodriguez_HW08_plot_viewer.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW08_plot_viewer
# Alternate CLI Usage: ./ARodriguez_HW08_plot_viewer.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL: https://youtu.be/-MwtKH-DKIQ
#
# Description:
# The program generates plot descriptions for stories through the
# following methods:
# - simple
# - random
# - interactive
#
# It achieves this by implementing a PlotViewer class that serves as the
# interface for registering plot generators and interacting with users.
# 
# The PlotViewer class abstracts away the complexities of generating
# plots and handles interactions between the user and the plot generators,
# allowing for flexible story creation.

# LIBRARIES
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


class InteractivePlotGenerator:
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
        selection = pv.queryUser(f"\nSelect desired first name for plot generation: ")
        choices.append(plot_names_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_adjectives_list]
        selection = pv.queryUser(f"\n\nSelect desired adjective for plot generation: \n")
        choices.append(plot_adjectives_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_professions_list]
        selection = pv.queryUser(f"\n\nSelect protagonist's desired profession for plot generation: \n")
        choices.append(plot_professions_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_verbs_list]
        selection = pv.queryUser(f"\n\nSelect desired verb for plot generation: \n")
        choices.append(plot_verbs_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_evil_adj_list]
        selection = pv.queryUser(f"\n\nSelect desired evil adjective for plot generation: \n")
        choices.append(plot_evil_adj_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_villain_job_list]
        selection = pv.queryUser(f"\n\nSelect antagonist's job for plot generation: \n")
        choices.append(plot_villain_job_list[int(selection)-1][0])

        [print(str(i[0]), end='\n') for i in plot_villains_list]
        selection = pv.queryUser(f"\n\nSelect antagonist's name for plot generation: \n")
        choices.append(plot_villains_list[int(selection)-1][0])

        return f"\t{choices[0]}, a {choices[1]} {choices[2]}, must {choices[3]} the {choices[4]} {choices[5]}, {choices[6]}."

class PlotViewer:
    """
    A class representing the viewer of plot generators.

    This class allows registration of different plot generator instances and facilitates generating plots
    using methods to ask for user input and to randomly make a selection.
    """

    def __init__(self):
        """Initialize a PlotViewer instance with no registered plot generator"""
        self.pg = None
        
    def registerPlotGenerator(self, pg):
        """
        Register a plot generator with the PlotViewer.

        Args:
        - pg (object): An instance of a plot generator to be registered.
        """
        self.pg = pg

    def generate(self):
        """
        Generate a plot using the registered plot generator.

        Returns:
        - str: The generated plot text.

        If no plot generator is registered, returns "No plot generator registered".
        """

        if self.pg:
            return self.pg.generate()
        else:
            return f"No plot generator registered"

    def queryUser(self, str):
        """
        Prompt the user for input.

        Args:
        - prompt (str): The prompt to display to the user.

        Returns:
        - str: The user's input.
        """

        return input(str)

    def random_choice(self, filename):
        """
        Select a random choice from the given file.

        Args:
        - filename (str): The name of the file containing choices.

        Returns:
        - str: The randomly selected choice.
        """

        choices = []
        with open(filename, 'r') as fin:
            data = [line.rstrip() for line in fin.readlines()]
            choices.append(random.choice(data))
        return choices

# MAIN PROGRAM FUNCTION
# Instantiate an object of the PlotViewer() class
pv = PlotViewer()

# Register each instantiaton of the plot generator objects
pv.registerPlotGenerator( SimplePlotGenerator() )

# Processes invoking the plot generation function for each object defined
print(pv.generate())

pv.registerPlotGenerator( RandomPlotGenerator() )
print(pv.generate())

pv.registerPlotGenerator( InteractivePlotGenerator() )
print(pv.generate())