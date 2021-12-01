import pandas as pd
import os

def Main():

    # Path that works from any computer
    rel_path = "../depth.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path)

    increments = 0
    prev_depth = df["Depth"].iloc[0]

    
    for depth in df["Depth"]:

        #print("Depth: " + str(depth))
        #print("Previous depth: " + str(prev_depth))

        if depth > prev_depth:
            increments += 1
        
        prev_depth = depth

    print(increments)
 
if __name__ == '__main__':
    Main()