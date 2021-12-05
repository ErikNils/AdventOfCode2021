#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import numpy as np
from Bingo_Number import Bingo_Number


def _board_bingo(board):
    for row in range(len(board)):
        row_flag = True
        col_flag = True
        for col in range(len(board)):
            if not board[row][col].bingo: row_flag = False
            if not board[col][row].bingo: col_flag = False
        if row_flag or col_flag: return True


def _score_counter(board):
    score = 0
    for row in board[0]:
        for col in row:
            if not col.bingo:
                score += int(col.number)
    return score*int(board[1])


def _board_interpreter(path):
    file = open(path,'r')
    
    board_list = []
    board = []
    
    bingo_nums = file.readline().rstrip().split(',')
    # Remove first empty line between bingo numbers and boards
    file.readline()
    
    for row in file:
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
    file.close()
    return board_list, bingo_nums


def _check_board(board, num, board_winners=None, index=None):
    for row in board:
        for col in row:
            if col.number == num:
                col.bingo = True
                if _board_bingo(board):
                    if board_winners: board_winners[index] = True
                    return (np.array(board), num)



def main():
    
    # Path that works from any computer
    rel_path = "../bingo.txt"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    
    board_list, bingo_nums = _board_interpreter(abs_path)
        
    winner = None
    
    # Check all boards if they need to mark a number
    for num in bingo_nums:
        for board in board_list:
            winner = _check_board(board, num)
            if winner: break
        if winner: break
    
    
    score = _score_counter(winner)
    print("Part 1:")
    print("The first winner has the score: " + str(score) + "\n")
                        
    #--------------- Part 2 ----------------------------------------
    
    board_winners = [False]*len(board_list)
    # Check the last board to win
    for num in bingo_nums:
        for index, board in enumerate(board_list):
            if board_winners[index]: continue
            winner = _check_board(board, num, board_winners, index)
   
    score = _score_counter(winner)
    print("Part 2:")
    print("Last board to win has a the score: " + str(score))

 
if __name__ == '__main__':
    main()