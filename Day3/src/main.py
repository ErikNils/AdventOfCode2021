#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os

def _gas_rating(df, gas):
    if gas not in ["carbon","oxygen"]:
        raise Exception("Invalid character in life support")
        
    
    ls = df["Bits"].tolist()
    bit_counts = 0
    
    for index in range(len(df["Bits"].iloc[0])):
        temp = []
        bit_counts = 0
        key_bit = None
        
        for bits in ls:
            if bits[index] == '1': bit_counts += 1
            elif bits[index] == '0': bit_counts -= 1
        
        # Evaluate if key_bit is '0' or '1'
        if bit_counts < 0:
            if gas == "carbon": key_bit = '1'
            elif gas == "oxygen": key_bit = '0'
        else:
            if gas == "carbon": key_bit = '0'
            elif gas == "oxygen": key_bit = '1'
        
        # Append bitstrings, whos bit matches key_bit, to the new list
        for bits in ls:
            if bits[index] == key_bit: temp.append(bits)
        
        ls = temp
        if len(ls) < 2:
            break
        
    return ls[0]
        
        

def main():
    
    # Path that works from any computer
    rel_path = "../bits.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path, dtype=str)
    
    # Creates a ls full of zeroes the length of the bitstrings
    ls = [0]*len(df["Bits"].iloc[0])
    
    # Counts '1' and '0' in each position
    for row in df.itertuples():
        for index, bit in enumerate(row.Bits):
            if bit == "1":
                ls[index] += 1
            elif bit == "0":
                ls[index] -= 1
    
    gamma_string = ""
    epsilon_string = ""
    
    # Convert list of bits counted into corresponding bitstrings
    for index, bit in enumerate(ls):
        if bit > 0:
            gamma_string += '1'
            epsilon_string += '0'
        else: 
            gamma_string += '0'
            epsilon_string += '1'
    
    # Convert bitstring to int
    gamma = int(gamma_string,2)
    epsilon = int(epsilon_string,2)
    
    print("Part 1:")
    print("Epsilon: " + str(epsilon))
    print("Gamma: " + str(gamma))
    print("Power consumption: " + str(epsilon*gamma) + "\n")
    
    #------------- Part 2 -----------------------------
    
    oxygen_str = _gas_rating(df, "oxygen")
    carbon_str = _gas_rating(df, "carbon")
    
    oxygen = int(oxygen_str, 2)
    carbon = int(carbon_str, 2)

    print("Part 2:")
    print("Oxygen rating: " + str(oxygen))
    print("Carbon rating: " + str(carbon))
    print("Life support rating: " + str(carbon*oxygen))
    

 
if __name__ == '__main__':
    main()