#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os

def main():
    
    # Path that works from any computer
    rel_path = "../commands.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path, sep = " ")
    
    # Data frames divided by commands.
    forward_df = df.loc[df["Command"] == "forward"]
    up_df = df.loc[df["Command"] == "up"]
    down_df = df.loc[df["Command"] == "down"]
    
    
    x_pos = sum(forward_df["Units"])
    depth = sum(down_df["Units"]) - sum(up_df["Units"])
    
    print("Part 1")
    print("Horizontal position: " + str(x_pos))
    print("Depth: " + str(depth))
    
    print("Product of horizontal position and depth: " + str(x_pos*depth))
    
    #---------- Part 2 ----------------------------------------------------
    
    aim = 0
    # Just resetting values of coordinates
    x_pos = 0
    depth = 0
    
    for row in df.itertuples():
        if row.Command == "forward":
            x_pos += row.Units
            depth += row.Units*aim
        elif row.Command == "up":
            aim -= row.Units
        elif row.Command == "down":
            aim += row.Units
            
    print("\nPart 2: ")
    print("Horizontal position: " + str(x_pos))
    print("Depth: " + str(depth))
    print("Product of horizontal position and depth: " + str(x_pos*depth))

 
if __name__ == '__main__':
    main()