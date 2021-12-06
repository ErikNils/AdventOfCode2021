#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().rstrip().split(',')]
    

# First function that scales increadibly bad
def _bad_lanterns(lanterns, days):
    for _ in range(days):
        for index, lantern in enumerate(lanterns):
            if lantern == 0:
                lanterns[index] = 6
                lanterns.append(9)
            else: lanterns[index] = lantern-1
    

# Second function that scales well
def _n_lanterns(lanterns, days):
    # Will hold the value of how many fishes have the same remaining days left
    fishes = [0]*10
    # Add starting fishes
    for lantern in lanterns:
        fishes[lantern] += 1
        
    for _ in range(days):
        
        new_fishes = fishes[0]
        
        # Lowers the days the fishes has until they give birth by 1
        for index in range(len(fishes)-1):
            fishes[index] = fishes[index+1]
        
        # Add the new fishes and the ones that just gave birth
        fishes[6] += new_fishes
        fishes[8] += new_fishes
        
        
    return sum(fishes)
        

def main():
    
    # Path that works from any computer
    rel_path = "../lanternfish.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    lanterns = read_integers(abs_path)
    
    print("Part 1:")
    lant = _n_lanterns(lanterns,80)
    print(str(lant) + "\n")
    
    #----- Part 2 ----------------------------------------------------------------
    
    #print(lanterns)
    lant = _n_lanterns(lanterns,256)
    print("Part 2:")
    print(lant)
    
  
 
if __name__ == '__main__':
    main()