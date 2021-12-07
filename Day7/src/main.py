#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import sys
import numpy as np

    
def _read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().rstrip().split(',')]
    
    
def _wrong_formula(dictionary):
    min_fuel = sys.maxsize
    
    for key, value in dictionary.items():
        new_fuel = 0
        for coord, crabs in dictionary.items():
            new_fuel += abs(coord-key)*crabs
        if new_fuel < min_fuel: min_fuel = new_fuel
    return min_fuel
    

def _lowest_fuel(dictionary):
    min_fuel = sys.maxsize
    
    for key in range(0, max(dictionary)+1):
        new_fuel = 0
        for coord, crabs in dictionary.items():
            steps = abs(coord-key)
            # Simplified form of 'new_fuel += np.arange(steps+1).sum()*crabs'
            # which is the first one i used that scales poorly
            new_fuel += (steps*(steps+1)//2)*crabs
        if new_fuel < min_fuel:
            min_fuel = new_fuel
            
    return min_fuel


    

def main():
    
    # Path that works from any computer
    rel_path = "../crabs.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    crabs = _read_integers(abs_path)
    
    dictionary = {}
    
    # Dictionary with coordinate of a crab as key and
    # the amount of crabs on that coordinate as value
    for coord in crabs:
        if coord in dictionary:
            dictionary[coord] += 1
        else: dictionary[coord] = 1
    
    print("Part 1:")
    min_fuel = _wrong_formula(dictionary)
    print("Minimum fuel with wrong formula: " + str(min_fuel) + "\n")
    #--------------- Part 2 ------------------------------------------

    min_fuel = _lowest_fuel(dictionary)
    print("Part 2:")
    print("Minimum fuel: " + str(min_fuel))
  
 
if __name__ == '__main__':
    main()