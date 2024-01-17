#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 01/15/2024
# Path: /mnt/c/Users/atone/Desktop/DPU-DSC430/HW1/A.Rodriguez_HW1_grading_logic.py
# Usage: /usr/bin/python3 ARodriguez_HW1_grading_logic.py
# Alternate Usage: /usr/bin/python3 -m ARodriguez_HW1_grading_logic
# Alternate CLI Usage: ./ARodriguez_HW1_grading_logic.py
# Git Repo URL: 
# Description:
# This program can be used to derive a subjective score based on a developer's
# self-assessment of the quality of their source code and against a list of 
# functional requirements.

# LIBRARIES:
import sys

# FUNCTIONS:
def results_check(result):
    """Function returns the earned point value as an integer for each functional
    or non-functional quality check being evaluated by the program, as well as a
    message indicating a PASS/FAIL result

    If quality check question relates requires a rating entry based on a
    numerical scale, an 'elif' condition is capable of handling the user entry.

    Args:
        result (str): A 'yes' or 'no' value entered by the end user as a response to 
                a code quality question, or an whole integer within the range
                of 1 - 10

    Attributes:
        earned_points (int): An value that represents points earned per
        functional or non-functional quality check

    Returns:
        earned_points (int): The numerical value of the total fixed points earned

    """
    if result.lower() == "yes":
        earned_points = 10
        print(f"  PASS...{earned_points} pts")
    elif result.lower() == "no":
        earned_points = 0
        print(f"  FAIL...{earned_points} pts")
        sys.exit()
    elif int(result) in range(0,11):
        earned_points = int(result)
        print(f"  SCORED...{earned_points} pts")
    else:
        print(f"  ERROR unexpected result.")

    return earned_points

def modular_check():
    """Function to self-check if single '.py' file was/will be submitted to D2L
    """
    result = input(f"- Was the assignment submitted as a single, uncompressed file with the '.py' extension? ")
    return results_check(result)

def author_heading_check():
    """Function to self-check if author's name exists wihtin file header

    Attributes:
        author_name_points (int): An value that represents points earned per
        functional or non-functional quality check
        
    Returns:
        (int): The sum of both the values of the 'author_name_points' and 
        'author_date_points' attributes

    """
    result = input(f"- Did the assignment include the author's name? ")

    author_name_points = results_check(result)

    def author_date_check():
        """Function to self-check if file creation date exists wihtin file header

        Attributes:
            author_date_points (int): An value that represents points earned per
            functional or non-functional quality check

        Returns:
            (int): The value of the 'author_date_points' attribute

        """
        result = input(f"- Did the assignment include the creation date? ")
        author_date_points = results_check(result)
        return author_date_points

    author_date_points = author_date_check()

    return author_name_points + author_date_points

def honor_stmt_check():
    """Function to self-check if the source code file includes a documented
    honor statement
    """
    result = input(f"- Did the assignment include the honor statement? ")

    return results_check(result)

def publish_link_check():
    """Function to self-check if a link to the code review video is included
    in the source code file
    """
    result = input(f"- Did the assignment include a published link to the code explanation video? ")

    return results_check(result)

def code_correctness_check():
    """Function to execute a self-check rating to determine if the source code
    logic was correctly implemented to achieve the intended objective
    """
    print(f"  NOTE: Consider how well the code aligns with the requirements and requested specifications")
    result = input(f"  - On a scale of 1 - 10, how would you evaluate the quality and accuracy of the code? ")

    return results_check(result)

def code_elegance_check():
    """Function to execute a self-check rating to determine if the source code
    meets minimum functional requirements and required specifications
    """
    print(f"  NOTE: Consider how functional and effectives the coding elements are within the execution of the program")
    result = input(f"  - How would you evaluate the elegance and effectiveness of the code? ")

    return results_check(result)

def code_hygiene_check():
    """Function to execute a self-check rating to determine if the source code
    was adequately formatted and structured for legibility and understanding
    """
    print(f"  NOTE: Consider the structure, legibility, and formatting of the source code")
    result = input(f"  - How would you evaluate the hygiene of the code? ")

    return results_check(result)

def feedback_discussion_quality_check():
    """Function to execute a self-check rating to determine if there was a
    satisfactory level of discussion and feedback being exchanged corresponding
    to the source code overview explanation 
    """
    print(f"  NOTE: Consider the published video explaining the execution of the program")
    result = input(f"  - How would you rate the quality of discussion and feedback regarding the code? ")

    return results_check(result)

def late_submission_check():
    """Function returns the earned point value as an integer for each functional
    or non-functional quality check being evaluated by the program, as well as a
    message indicating a PASS/FAIL result

    This is a function to execute a self-check rating to determine if the
    assignment was submitted to D2L on-time

    Attributes:
        earned_points (int): An value that represents points earned
        ontime_submission_points (int): The points earned for submitting the
            assignment
        late_penalty_points (int): A value that represents the points to be 
            

    Returns:
        (int): The sume of the points earned for submitting the assignment
        on-time minus any late penalty deductions

    """
    result = input(f"- Was the assignment file submitted on time (yes/no)? ")
    earned_points = int(10)
    print(f"  PASS...{earned_points} pts")

    ontime_submission_points = earned_points

    if result.lower() == "no":
        def late_penalty_deductions():
            """Function returns the points to be deducted from the total of
            earned points due to a late assignment submission

            Attributes:
                late_penalty (int): A self-assessed points value for a late
                submission based on how many hours the assignment is late

            Returns:
                late_penalty (int): A value that represents the points to be 
                deducted for submitting a late assignment

           """
            late_penalty = int(input(f"- In hours, how late was the assignment submission (1-96)? "))
            print(f"  DEDUCTION...{late_penalty} pts")
            return late_penalty

        late_penalty_points = late_penalty_deductions()
    else:
        late_penalty_points = 0

    return ontime_submission_points + (-late_penalty_points)


# MAIN PROGRAM:
def calculate_score():
    """Function returns the percentage total points earned, possible points, and score

    Attributes:
        max_points (int): A maximum number of possible points to be earned
        earned_points (int): A number of points earned after passing code quality checks
        modular_check_points (int): A number of points earned after passing modular check
        author_heading_points (int): A number of points earned after passing author heading check
        honor_stmt_check_points (int): A number of points earned after passing honor statement check
        publish_link_points (int): A number of points earned after passing published link check
        code_correctness_points (int): A number of points earned after passing a code correctness check
        code_elegance_points (int): A number of points earned after passing a code elegance check
        code_hygiene_points (int): A number of points earned after passing a code hygiene check
        feedback_discussion_quality_points (int): A number of points after passing a feedback check
        late_penalty_points (int): A number of points after assessing for a late submission
        total_earned_points (int): A sum of all points earned for all checks
        score (int): A percentage of total earned points divided by the total possible, or max points

    Returns:
        score (int): A percentage of total earned points divided by the total possible, or max points

    """
    # Declaration of global variables
    global max_points
    global earned_points
    global late_penalty_points

    # Initialization of global variables
    max_points = 100
    earned_points = 0
    late_penalty_points = 0

    # Function calls for all functional requirement code quality checks
    print(f"Please answer the following set of questions with a 'yes' or 'no' entry: ")
    modular_check_points = modular_check()
    author_heading_points = author_heading_check()
    honor_stmt_check_points = honor_stmt_check()
    publish_link_points = publish_link_check()
    print(f"\n")

    # Function calls for all non-functional requirement code quality checks
    print(f"For the following set of questions, rate your response on a scale of 1 - 10: ")
    code_correctness_points = code_correctness_check()
    code_elegance_points = code_elegance_check()
    code_hygiene_points = code_hygiene_check()
    feedback_discussion_quality_points = feedback_discussion_quality_check()
    print(f"\n")

    # Function call for late submission check
    print(f"Assessing submission for late penalty deductions...")
    late_penalty_points = late_submission_check()
    print(f"\n")

    # A sum of all points returned from each funtional/non-functional source code quality check
    total_earned_points = (modular_check_points +\
                            author_heading_points +\
                            honor_stmt_check_points +\
                            publish_link_points +\
                            code_correctness_points +\
                            code_elegance_points +\
                            code_hygiene_points +\
                            feedback_discussion_quality_points) + late_penalty_points

    # A calculation for the total earned score as a fraction of the total possible points
    score = total_earned_points/max_points

    # Result summary including total earned points, maximum points, and a score percentages
    print(f"Evaluation Results:")
    print(f"\tTotal Earned Points: {total_earned_points}\n\
    \tTotal Possible Points: {max_points}")

    return score


# Primary function call that invokes the main function
if __name__ == "__main__":
    score = calculate_score()

    # Course grading scale
    if score >= 0.90:
        grade = 'A'
    elif score >= 0.80 and score < 0.90:
        grade = 'B'
    elif score >= 0.70 and score < 0.80:
        grade = 'C'
    elif score >= 0.60 and score < 0.70:
        grade = 'D'
    elif score < 0.60:
        grade = 'F'
    else:
        print("Incomplete assignment")

    # Grade and percentage earned for assignment submission
    print(f"\nAssignment Grade: {grade} - {score:.0%}")

# TODO:
# - [ ] TODO: Add bool variable to show if check is a functional requirement 
# - [ ] TODO: Add bool variable to show if check validates adherance to coding standards (non-functional)
# - [ ] TODO: Add function to parse target file for number of lines containing pattern: 'TODO' 
# - [ ] TODO: Print quality check name, pass/fail, and points in line
# - [ ] TODO: Remove quality check name, pass/fail, and points and instead print info as a summary of results
# - [ ] TODO: Add function to only run runctional requirement checks and output percentage score accordingly
# - [ ] TODO: Add function to only run non-functional checks and output percentage score accordingly
# - [ ] TODO: Add function to score a single file when filename is passed as parameter
# - [ ] TODO: Add function to score a multiple files when directory name is passed as parameter
# - [ ] TODO: Add function to output scores to .txt files named by the input filename
# - [ ] TODO: Add function to check for Google-style python docstrings (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google)
# - [ ] TODO: Add regex logic to parse different elements of the source code, including commented headers, functions, classes, in-line comments
