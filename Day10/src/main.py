#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
from collections import deque





def _read_file(path):
    file = open(path,'r')
    clean = []
    corr = 0
    discard = False
    for line in file:
        arr = list(line.strip())
        tmp, discard = _corrupted(arr)
        corr += tmp
        if not discard: clean.append(arr)
    file.close()
    incomplete = _completion(clean)
    
    return corr,incomplete


def _corrupted(arr):
    stack = deque()
    values = {')':3,']':57,'}':1197,'>':25137}
    for ele in arr:
        if ele == '(': stack.append(')')
        elif ele == '[': stack.append(']')
        elif ele == '{': stack.append('}')
        elif ele == '<': stack.append('>')
        elif ele != stack.pop(): return values[ele],True
    return 0,False


def _completion(arrs):
    scores = []
    stack = deque()
    values = {')':1,']':2,'}':3,'>':4}
    for arr in arrs:
        res = 0
        for ele in arr:
            if ele == '(': stack.append(')')
            elif ele == '[': stack.append(']')
            elif ele == '{': stack.append('}')
            elif ele == '<': stack.append('>')
            else: stack.pop()
        while len(stack) > 0:
            res *= 5
            res += values[stack.pop()]
        scores.append(res)
    scores = sorted(scores)
    return scores[(len(scores)//2)]
        

def main():
    
    # Path that works from any computer
    rel_path = "../chunks.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    corr,incomplete = _read_file(abs_path)
    print("Part 1:")
    print("Corrupted score: " + str(corr) + "\n")
    #------------- Part 2 ----------------------------------------
    print("Part 2:")
    print("Incomplete score: " + str(incomplete))

 
if __name__ == '__main__':
    main()