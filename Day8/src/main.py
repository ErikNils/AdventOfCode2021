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
    
    result = 0
    for segment in segments:
        x = _def_signals(segment)
        ls = []
        seg_codes = {}
        # Getting the charactar combination for each value
        ls.append("".join(sorted(x[0]+x[1]+x[2]+x[4]+x[5]+x[6])))
        ls.append("".join(sorted(x[2]+x[5])))
        ls.append("".join(sorted(x[0]+x[2]+x[3]+x[4]+x[6])))
        ls.append("".join(sorted(x[0]+x[2]+x[3]+x[5]+x[6])))
        ls.append("".join(sorted(x[1]+x[2]+x[3]+x[5])))
        ls.append("".join(sorted(x[0]+x[1]+x[3]+x[5]+x[6])))
        ls.append("".join(sorted(x[0]+x[1]+x[3]+x[4]+x[5]+x[6])))
        ls.append("".join(sorted(x[0]+x[2]+x[5])))
        ls.append("".join(sorted(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6])))
        ls.append("".join(sorted(x[0]+x[1]+x[2]+x[3]+x[5]+x[6])))

        # Adding the char comb to a value in a dictionary
        for index, code in enumerate(ls):
            seg_codes[code] = index
        print(seg_codes)
        
        res = 0
        for index, output in enumerate(segment[1]):
            code = "".join(sorted(output))
            print("This is the code: " + code)
            this_shit = seg_codes[code]*pow(10,(len(segment[1])-index-1))
            print("This shit: " + str(this_shit))
            res += this_shit
        print("This is res: " + str(res))
        result += res
    return result




# Need to map signals for each segment

def _def_signals(segment):
    segs = segment[0]+segment[1]
    signals_list = []
    for i in range(7):
        signals_list.append([])
    # First we add the signals to the places we know they can be
    for signals in segs:
        tmp = []
        for signal in signals:
                tmp.append(signal)
        if len(tmp) == 2:
            signals_list[2] = _overlaps(tmp,signals_list[2])
            signals_list[5] = _overlaps(tmp,signals_list[5])
        elif len(tmp) == 3:
            signals_list[0] = _overlaps(tmp,signals_list[0])
            signals_list[2] = _overlaps(tmp,signals_list[2])
            signals_list[5] = _overlaps(tmp,signals_list[5])
        elif len(tmp) == 4:
            signals_list[1] = _overlaps(tmp,signals_list[1])
            signals_list[2] = _overlaps(tmp,signals_list[2])
            signals_list[3] = _overlaps(tmp,signals_list[3])
            signals_list[5] = _overlaps(tmp,signals_list[5])
        elif len(tmp) == 5:
            signals_list[0] = _overlaps(tmp,signals_list[0])
            signals_list[3] = _overlaps(tmp,signals_list[3])
            signals_list[6] = _overlaps(tmp,signals_list[6])
        elif len(tmp) == 6:
            signals_list[0] = _overlaps(tmp,signals_list[0])
            signals_list[1] = _overlaps(tmp,signals_list[1])
            signals_list[5] = _overlaps(tmp,signals_list[5])
            signals_list[6] = _overlaps(tmp,signals_list[6])
        else:
            continue
    # Uses process of elimination to find remaining signals (yes this works for all segments)
    signals_list[6].remove(signals_list[0][0])
    signals_list[1].remove(signals_list[5][0])
    signals_list[2].remove(signals_list[5][0])
    tmp = ['a','b','c','d','e','f','g']
    for signal in signals_list:
        if signal == []: continue
        tmp.remove(signal[0])
    signals_list[4] = tmp
    # Just removing one layer of 'list'
    for i in range(7):
        signals_list[i] = signals_list[i][0]
    #print("List of signals: " + str(signals_list))
    return signals_list

                    
    
def _overlaps(signals1,signals2):
    if signals2 == []: return signals1
    new_signals = []
    for signal in signals1:
        if signal in signals2: new_signals.append(signal)
    if new_signals == []: return signals2
    else: return new_signals



def main():
    
    # Path that works from any computer
    rel_path = "../segments.csv"
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