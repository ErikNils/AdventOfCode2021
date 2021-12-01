import pandas as pd
import os
import numpy as np

def Main():

    # Path that works from any computer
    rel_path = "../depth.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path)

    increments = 0
    # Make prev_depth the max value of the given type
    prev_depth = np.iinfo(df["Depth"].iloc[0].dtype).max

    #------------ Part 1 -------------------------------------------
    for depth in df["Depth"]:

        #print("Depth: " + str(depth))
        #print("Previous depth: " + str(prev_depth))

        if depth > prev_depth: increments += 1
        
        prev_depth = depth

    print(increments)
    #----------------------------------------------------------------

    #------------- Part 2 -------------------------------------------

    sum_incs = 0
    # Make prev_sum the max value of given type
    prev_sum = np.iinfo(df["Depth"].iloc[0].dtype).max
    new_sum = 0
    
    # Counting 3 elements at a time so loop needs to be 2 iterations shorter
    for index in range(len(df["Depth"]) - 2):
        # Add togeather new sum
        new_sum = df["Depth"].iloc[index]
        new_sum += df["Depth"].iloc[index+1]
        new_sum += df["Depth"].iloc[index+2]

        if new_sum > prev_sum: sum_incs +=1
        
        prev_sum = new_sum
    
    print(sum_incs)

 
if __name__ == '__main__':
    Main()