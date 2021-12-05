#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os
import numpy as np

# Oh god this looks ugly
def _diagonal(range_row, range_col, board):
    col_incs = []
    row_incs = []
    
    # Needed for range to automatically detect if it needs to increase or decrease numbers.
    row_sign = int(abs(range_row[1]-range_row[0])/(range_row[1]-range_row[0]))
    col_sign = int(abs(range_col[1]-range_col[0])/(range_col[1]-range_col[0]))
    
    for row in range(range_row[0], range_row[1]+row_sign, row_sign):
        row_incs.append(row)
    for col in range(range_col[0], range_col[1]+col_sign, col_sign):
        col_incs.append(col)
    for index in range(0,len(row_incs)):
        board[row_incs[index]][col_incs[index]] += 1
        
        
        
def _lines(df, board, diag = True):
    for serie in df.itertuples():
        range_row = (serie.x1,serie.x2)
        range_col = (serie.y1,serie.y2)
        # If the line is diagonal we ignore it
        if max(range_row) != min(range_row) and max(range_col) != min(range_col): 
            if diag: _diagonal(range_row, range_col, board)
            else: continue
        
        else:
            for row in range(min(range_row), max(range_row)+1):
                for col in range(min(range_col), max(range_col)+1):
                    board[row][col] += 1
                    
                    
def _overlaps(board):
    overlap = 0
    for row in board:
        for col in row:
            if col > 1: overlap += 1
    return overlap
    
    

def main():
    
    # Path that works from any computer
    rel_path = "../lines.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    df = pd.read_csv(abs_path, sep = ",|->", names = ["x1","y1","x2","y2"], engine = "python")


    board = np.array([[0]*1000]*1000)
    
    # Exclude diagonals
    _lines(df,board, False)
            
    print("Part 1:")
    print("Overlaps excluding diagonals: " + str(_overlaps(board)) + "\n")
    #--------------- Part 2 ----------------------------------------------------------------
    
    board = np.array([[0]*1000]*1000)
    
    # Include diagonals
    _lines(df, board)
    
    print("Part 2:")
    print("Overlaps including diagonals: " + str(_overlaps(board)))
    
 
if __name__ == '__main__':
    main()