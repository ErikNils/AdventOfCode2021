#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os

def Main():
    
    # Path that works from any computer
    rel_path = "../bits.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path, dtype=str)
    
    # Creates a list full of zeroes the length of the bitstrings
    list = [0]*len(df["Bits"].iloc[0])
    
    # Counts '1' and '0' in each position
    for row in df.itertuples():
        for index, bit in enumerate(row.Bits):
            if bit == "1":
                list[index] += 1
            elif bit == "0": list[index] -= 1
    
    gamma_string = ""
    epsilon_string = ""
    
    for index, bit in enumerate(list):
        if bit > 0:
            gamma_string += '1'
            epsilon_string += '0'
        else: 
            gamma_string += '0'
            epsilon_string += '1'
    #print(list)
    #print(gamma_string)
    #print(epsilon_string)
    
    gamma = int(gamma_string,2)
    epsilon = int(epsilon_string,2)
    
    print("Epsilon: " + str(epsilon))
    print("Gamma: " + str(gamma))
    print("Power consumption: " + str(epsilon*gamma))
    
    #------------- Part 2 -----------------------------
    
   

 
if __name__ == '__main__':
    Main()