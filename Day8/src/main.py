#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import sys
import numpy as np




def _read_file(filename):
    rows = []
    with open(filename) as file:
        for row in file:
            line = row.strip().split("|")
            line[0] = line[0].strip().split(" ")
            line[1] = line[1].strip().split(" ")
            rows.append(line)
    return rows

def _count_outputs(segments):
    counter = 0
    valids = [2,3,4,7]
    for outputs in segments:
        for output in outputs[1]:
            if len(output) in valids: counter += 1
    return counter



def _sum_output(segments):
    # This looks kinda fugly, ngl
    ls = []
    seg_codes = {}
    ls.append("".join(sorted("cagedb")))
    ls.append("".join(sorted("ab")))
    ls.append("".join(sorted("gcdfa")))
    ls.append("".join(sorted("fbcad")))
    ls.append("".join(sorted("eafb")))
    ls.append("".join(sorted("cdfbe")))
    ls.append("".join(sorted("cdfgeb")))
    ls.append("".join(sorted("dab")))
    ls.append("".join(sorted("acedgfb")))
    ls.append("".join(sorted("cefabd")))
    
    for index, code in enumerate(ls):
        print(code)
        seg_codes[code] = index
    print(seg_codes)
    result = 0
    for outputs in segments:
        res = 0
        for index, output in enumerate(outputs[1]):
            code = "".join(sorted(output))
            print("This is the code: " + code)
            this_shit = seg_codes[code]*pow(10,(len(outputs[1])-index-1))
            print("This shit: " + str(this_shit))
            res += this_shit
        print("This is res: " + str(res))
        result += res
    return result

# Need to map signals for each segment




def main():
    
    # Path that works from any computer
    rel_path = "../example.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    segments = _read_file(abs_path)
    print(segments)
    outputs = _count_outputs(segments)
    
    
    print("Part 1:")
    print(outputs)
    print("\n")
    #--------------- Part 2 ------------------------------------------

    print("Part 2:")
    output_sum =_sum_output(segments)
    print(output_sum)
 
if __name__ == '__main__':
    main()