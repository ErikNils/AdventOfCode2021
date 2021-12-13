#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import numpy as np
from Octopus import Octopus





def _read_file(path):
    file = open(path,'r')
    
    matrix = []
    
    for line in file:
        arr = list(line.strip())
        for i,ele in enumerate(arr):
            arr[i] = Octopus(int(ele))
        matrix.append(arr)
    return np.array(matrix)


def _flashes_sum(matrix, steps):
    flashes = 0
    # Iterates over all octopuses
    for step in range(steps):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                octopus = matrix[row][col]
                octopus.number += 1
                if not octopus.flash and octopus.number > 9:
                    flashes += _flash(row,col,matrix)
        # Check if all octopuses flashes at the same time
        counter = 0
        for row in matrix:
            for octopus in row:
                if octopus.flash:
                    octopus.flash = False
                    octopus.number = 0
                    counter += 1
        if counter == 100: return flashes, step+1
    return flashes, steps



def _flash(r,c,matrix):
    octopus = matrix[r][c]
    octopus.flash = True
    flashes = 1
    # Increment flash counter for adjacent octopuses
    for row in range(r-1,r+2):
        for col in range(c-1,c+2):
            if _conditions(row,col,matrix): continue
            adj_oct = matrix[row][col]
            adj_oct.number += 1
            if adj_oct.flash is not True and adj_oct.number > 9:
                flashes += _flash(row,col,matrix)
    return flashes
    
    

# Ignores out of bounds nodes
def _conditions(row,col,matrix):
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1: return True
    return False




def main():
    
    # Path that works from any computer
    rel_path = "../energy.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    matrix = _read_file(abs_path)
    flashes,steps = _flashes_sum(matrix,250)
    print("Part 1:")
    print("Number of flashes: " + str(flashes) + "\n")

    #--------- Part 2 --------------------------------------------------
    
    print("Part 2:")
    print("Synchronized after: " + str(steps) + " steps")
   

 
if __name__ == '__main__':
    main()