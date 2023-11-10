import os
import time
import copy

def checkStatus(A,x,y):
    aliveNeighbors = 0
    if x-1 >= 0 and y-1 >= 0:
        if A[x-1][y-1] == '⬜':
            aliveNeighbors += 1

    if y-1 >= 0:
        if A[x][y-1] == '⬜':
            aliveNeighbors += 1


    if y-1 >= 0:
        try:
            if A[x+1][y-1] == '⬜':
                aliveNeighbors += 1
        except:
            pass

    if x-1 >= 0:
        if A[x-1][y] == '⬜':
            aliveNeighbors += 1

    try:
        if A[x+1][y] == '⬜':
            aliveNeighbors += 1
    except:
        pass

    if x-1 >= 0:
        try:
            if A[x-1][y+1] == '⬜':
                aliveNeighbors += 1
        except:
            pass
    try:
        if A[x][y+1] == '⬜':
            aliveNeighbors += 1
    except:
        pass
    try:
        if A[x+1][y+1] == '⬜':
            aliveNeighbors += 1
    except:
        pass
    
    if A[x][y] == '⬜':
        if aliveNeighbors == 2 or aliveNeighbors == 3:
            return '⬜'
        else:
            return '⬛'
    else:
        if aliveNeighbors == 3:
            return '⬜'
        else:
            return '⬛'

board = [["⬛" for i in range(41)]for j in range (20)]
board[5][1+1] = "⬜"
board[5][2+1] = "⬜"
board[6][1+1] = "⬜"
board[6][2+1] = "⬜"
board[5][11+1] = "⬜"
board[6][11+1] = "⬜"
board[7][11+1] = "⬜"
board[8][12+1] = "⬜"
board[4][12+1] = "⬜"
board[3][13+1] = "⬜"
board[9][13+1] = "⬜"
board[9][14+1] = "⬜"
board[3][14+1] = "⬜"
board[6][15+1] = "⬜"
board[6][17+1] = "⬜"
board[6][18+1] = "⬜"
board[5][17+1] = "⬜"
board[4][16+1] = "⬜"
board[8][16+1] = "⬜"
board[7][17+1] = "⬜"
board[3][21+1] = "⬜"
board[4][21+1] = "⬜"
board[5][21+1] = "⬜"
board[3][22+1] = "⬜"
board[4][22+1] = "⬜"
board[5][22+1] = "⬜"
board[6][23+1] = "⬜"
board[2][23+1] = "⬜"
board[2][25+1] = "⬜"
board[1][25+1] = "⬜"
board[6][25+1] = "⬜"
board[7][25+1] = "⬜"
board[2][25+1] = "⬜"
board[4][36] = "⬜"
board[3][37] = "⬜"
board[3][36] = "⬜"
board[4][37] = "⬜"
nextBoard = [[None for i in range(41)]for j in range (20)]

os.system('cls')

for row in board:
    for element in row:
        print(element,end='')
    print()

while(True):
    for i in range(len(board)):
        for j in range(len(board[0])):
            nextBoard[i][j] = checkStatus(board,i,j)
    time.sleep(0.05)
    os.system('cls')
    board = copy.deepcopy(nextBoard)
    for row in board:
        for element in row:
            print(element,end='')
        print()

