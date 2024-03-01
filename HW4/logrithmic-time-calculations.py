#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/08/2024
# Usage: /usr/bin/python3 ARodriguez_HW_test.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW_test
# Alternate CLI Usage: ./ARodriguez_HW_test.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
import math

# FUNCTIONS
def example1(list):
    m = 0
    for i in range(len(list)):test
        m += list[i]
    return m

def example2(list):
    m = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if (list[i] == list[j]):
                m += 1
    return m

def example3(list):
    m = 0
    for i in range(len(list)):
        for j in range(0, i - 1):
            if (list[i] == list[j]):
                m += 1
    return m

def example4(list):
    m = 0
    n = len(list)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m += 1
    return m

def example5(list):
  m = 0
  n = len(list)
  for i in range(n):
    for j in range(int(math.sqrt(n))):
      m += 1
  return m

def example6(list):
  m = 0
  for i in range(len(list)):
    for j in range( int(math.sqrt(1087)) ):
      m += 1
  return m

def example7(list):
  m = 0
  for i in range(len(list)):
    m += doThing(list)
  return m

def doThing(list):
  m = 0
  for i in range(len(list)):
    m += 1
  return m

def example8(list):
  m = 0
  for i in range(len(list)):
    m += doThing(list)
  return m

def doThing(list):
  return list[0]

def example9(list):
  m = 0
  i = 1
  n = len(list)
  while i < n:
    m += 1
    i = i * 2
  return m

def example10(list):
  m = 0
  i = len(list)
  while i > 1:
    m += 1
    i = i / 2
  return m

# MAIN PROGRAM FUNCTION
def main():
    print(f"Running example 1: {example1([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 2: {example2([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 3: {example3([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 4: {example4([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 5: {example5([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 6: {example6([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 7: {example7([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 8: {example8([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 9: {example9([0,1,2,3,4,5,6,7,8,9])}")

    print(f"Running example 10: {example10([0,1,2,3,4,5,6,7,8,9])}")

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main()

