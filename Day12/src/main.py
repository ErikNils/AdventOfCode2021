#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import numpy as np
from collections import defaultdict, deque





def _read_file(path):
    file = open(path,'r')
    
    caves = defaultdict(set)    
    
    for line in file:
        x,y = line.strip().split("-")
        caves[x].add(y)
        caves[y].add(x)
    file.close()
    
    return caves

def _paths(caves,flag = False):
    start = ('start', set(['start']), None)
    stack = deque([start])
    paths = 0
    
    while stack:
        cave, small_caves, twice = stack.pop()
        if cave == 'end':
            paths += 1
            continue
        for adjacent in caves[cave]:
            if adjacent not in small_caves:
                tmp = set(small_caves)
                if adjacent.islower(): tmp.add(adjacent)
                stack.append((adjacent,tmp,twice))
            elif _condition(adjacent,small_caves,twice,flag):
                stack.append((adjacent,small_caves,adjacent))
    return paths

def _condition(cave,small_caves,twice,flag):
    return cave in small_caves and twice is None and cave not in ['start','end'] and flag
    



def main():
    
    # Path that works from any computer
    rel_path = "../paths.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    caves = _read_file(abs_path)
    paths = _paths(caves)
    print("Part 1:")
    print("Number of paths: " + str(paths) + "\n")

    #--------- Part 2 --------------------------------------------------
    
    print("Part 2:")
    paths = _paths(caves,True)
    print("Number of paths: " + str(paths))

 
if __name__ == '__main__':
    main()