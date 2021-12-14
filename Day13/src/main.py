#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os
import numpy as np



def _read_file(path,example=False):
    file = open(path,'r')
    if example: sheet = np.array([[False]*11]*15)
    else: sheet = np.array([[False]*1311]*895)
    commands = []
    flag = False
    
    for line in file:
        if line.strip() == "": 
            flag = True
            continue
        if flag:
            commands.append(line.strip().split(" ")[2].split("="))
        else: 
            x,y = line.strip().split(",")
            sheet[int(y)][int(x)] = True
    file.close()
    #print(sheet)
    #print(commands)
    return sheet,commands

def _fold(sheet,commands,flag=100):
    dots = 0
    counter = 0
    for command in commands:
        if counter >= flag: break
        counter += 1
        if command[0] == 'x':
            sheet = _fold_left(sheet)
        else:
            sheet = _fold_up(sheet)
    for row in sheet:
        for col in row:
            if col: dots += 1
    return dots,sheet


def _fold_left(sheet):
    for row in range(len(sheet)):
        for col in range(len(sheet[0])-1, len(sheet[0])//2,-1):
            sheet[row][len(sheet[0])-1-col] = sheet[row][len(sheet[0])-1-col] or sheet[row][col]
    new_sheet = []
    for row in sheet:
        new_sheet.append(row[:len(sheet[0])//2])
    return np.array(new_sheet)



def _fold_up(sheet):
    for row in range(len(sheet)-1, len(sheet)//2,-1):
        for col in range(len(sheet[0])):
            sheet[len(sheet)-1-row][col] = sheet[len(sheet)-1-row][col] or sheet[row][col]
    return sheet[:len(sheet)//2]


def main():
    
    # Path that works from any computer
    rel_path = "../instructions.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    sheet,commands =_read_file(abs_path)
    dots,sheet = _fold(sheet,commands,1)
    print("Part 1:")
    print("Dots after first fold: " + str(dots) + "\n")

    #--------- Part 2 --------------------------------------------------
    sheet,commands =_read_file(abs_path)
    dots,sheet = _fold(sheet,commands)
    print("Part 2:")
    for row in sheet:
        string = ""
        for col in row:
            if col: string += '#'
            else: string += '.'
        print(string)
    

 
if __name__ == '__main__':
    main()