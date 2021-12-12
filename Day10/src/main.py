#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
from posixpath import abspath
import numpy as np





def _read_file(path):
    file = open(path,'r')
    
    for line in file:
        arr = list(line.strip())
        print(arr)
    file.close()
    return 


def _corrupted(arr):
    para = 0
    clam = 0
    curl = 0
    gap = 0
    for ele in arr:
        if ele == '(': para += 1
        elif ele == ')':
            para -= 1
            if para < 0: return 3
        elif ele == '[': clam += 1
        elif ele == ']':
            clam -= 1
            if clam < 0: return 57
        elif ele == '{': curl += 1
        elif ele == '}':
            curl -= 1
            if curl < 0: return 1197
        elif ele == '<': gap += 1
        elif ele  == '>':
            gap -= 1
            if gap < 0: return 25137


def main():
    
    # Path that works from any computer
    rel_path = "../example.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    _read_file(abs_path)

 
if __name__ == '__main__':
    main()