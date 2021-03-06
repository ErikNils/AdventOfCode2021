#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import numpy as np
from Point import Point





def _read_file(path):
    file = open(path,'r')
    
    matrix = []
    
    for line in file:
        arr = list(line.strip())
        for i,ele in enumerate(arr):
            arr[i] = Point(int(ele))
        matrix.append(arr)
    return np.array(matrix)


def _risk_level(matrix):
    result = 0
    low_list = []
    lowpoint = True
    # Iterates over adjacent, except diagonal, nodes
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            low = matrix[r][c]
            for row in range(r-1,r+2):
                for col in range(c-1,c+2):
                    if _conditions(row,col,r,c,matrix): continue
                    adj = matrix[row][col]
                    if adj.number <= low.number:
                        lowpoint = False
                        break
                if not lowpoint:
                    break
            if lowpoint: 
                result += low.number+1
                low_list.append((r,c))
            lowpoint = True
    return result, low_list


# Ignores out of bounds and diagonal nodes
def _conditions(row,col,r,c,matrix):
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1: return True
    elif (row < r and col != c) or (row > r and col != c) or (row == r and col == c): return True
    return False




def _basin(r,c,matrix,sum):
    if matrix[r][c].checked is True: return sum
    sum += 1
    matrix[r][c].checked = True
    for row in range(r-1,r+2):
        for col in range(c-1,c+2):
            if _conditions(row,col,r,c,matrix): continue
            adj = matrix[row][col]
            if adj.number < 9:
                sum = _basin(row,col,matrix,sum)
    return sum



def main():
    
    # Path that works from any computer
    rel_path = "../smoke.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    matrix = _read_file(abs_path)
    #print(matrix)
    sum, low_list = _risk_level(matrix)
    print("Part 1:")
    print("Sum of risk levels: " + str(sum) + "\n")

    #--------- Part 2 --------------------------------------------------
    basins = []
    for row,col in low_list:
        basins.append(_basin(row,col,matrix,0))
    basins = sorted(basins, reverse=True)
    result = 1
    for basin in basins[:3]:
        result *= basin
    print("Part 2:")
    print("Product of 3 largest basins: " + str(result))

 
if __name__ == '__main__':
    main()