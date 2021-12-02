#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os
import numpy as np

def Main():
    
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
    
    print("Horizontal position: " + str(x_pos))
    print("Depth: " + str(depth))
    
    print("Product of horizontal position and depth: " + str(x_pos*depth))
    
    #---------- Part 2 ----------------------------------------------------
    
    

 
if __name__ == '__main__':
    Main()