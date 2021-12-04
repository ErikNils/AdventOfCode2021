#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import pandas as pd
import os
import numpy as np
from Bingo_Number import Bingo_Number


def board_bingo(board):
    
    for row in range(len(board)):
        row_flag = True
        col_flag = True
        for col in range(len(board)):
            if board[row][col].bingo == False: row_flag = False
            if board[col][row].bingo == False: col_flag = False
        if row_flag or col_flag: return True


def score_counter(board):
    score = 0
    for row in board[0]:
        for col in row:
            if not col.bingo:
                score += int(col.number)
    return score*int(board[1])


def board_interpreter(path):
    f = open(path,'r')
    
    board_list = []
    board = []
    
    bingo_nums = f.readline().rstrip().split(',')
    # Remove first empty line between bingo numbers and boards
    f.readline()
    
    for row in f:
        row_ls = row.strip().split()
        #print("Row_ls: " + str(row_ls))
        bingo_row = []
        for num in row_ls: bingo_row.append(Bingo_Number(num))
        if row_ls == []:
            #print("Board: " + str(board))
            board_list.append(board)
            board = []
        else: 
            board.append(bingo_row)
    f.close()
    return board_list, bingo_nums


def check_board(board, num, board_winners=None, index=None):
    for row in board:
        for col in row:
            if col.number == num:                      
                col.bingo = True
                if board_bingo(board):
                    if board_winners: board_winners[index] = True
                    return (np.array(board), num)



def Main():
    
    # Path that works from any computer
    rel_path = "../bingo.txt"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    
    board_list, bingo_nums = board_interpreter(abs_path)
        
    winner = None
    
    # Check all boards if they need to mark a number    
    for num in bingo_nums:
        for board in board_list:
            winner = check_board(board, num)
            if winner: break
        if winner: break
    
    
    score = score_counter(winner)
    print("The first winner has the score: " + str(score))
                        
    #--------------- Part 2 ----------------------------------------
    
    board_winners = [False]*len(board_list)
    # Check the last board to win
    for num in bingo_nums:
        for index, board in enumerate(board_list):
            if board_winners[index]: continue
            winner = check_board(board, num, board_winners, index)
   
    score = score_counter(winner)
    print("Last board to win has a the score: " + str(score))

 
if __name__ == '__main__':
    Main()