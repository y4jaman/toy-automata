import tkinter as tk
import os
import time
import copy


GRID_SIZE = 70
CELL_SIZE = 10
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

board = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
nextBoard = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def update_delay(value):
    global delay
    delay = int(value)

def checkStatus(A,x,y):
    aliveNeighbors = 0
    if x-1 >= 0 and y-1 >= 0:
        if A[x-1][y-1] == True:
            aliveNeighbors += 1

    if y-1 >= 0:
        if A[x][y-1] == True:
            aliveNeighbors += 1


    if y-1 >= 0:
        try:
            if A[x+1][y-1] == True:
                aliveNeighbors += 1
        except:
            pass

    if x-1 >= 0:
        if A[x-1][y] == True:
            aliveNeighbors += 1

    try:
        if A[x+1][y] == True:
            aliveNeighbors += 1
    except:
        pass

    if x-1 >= 0:
        try:
            if A[x-1][y+1] == True:
                aliveNeighbors += 1
        except:
            pass
    try:
        if A[x][y+1] == True:
            aliveNeighbors += 1
    except:
        pass
    try:
        if A[x+1][y+1] == True:
            aliveNeighbors += 1
    except:
        pass
    
    if A[x][y] == True:
        if aliveNeighbors == 2 or aliveNeighbors == 3:
            return True
        else:
            return False
    else:
        if aliveNeighbors == 3:
            return True
        else:
            return False

def toggle_cell_state(row, col):
    board[row][col] = not board[row][col]
    color = "black" if board[row][col] else "white"
    canvas.itemconfig(cell_rectangles[row][col], fill=color)

def on_cell_click(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    toggle_cell_state(row, col)

def start_simulation():
    global board
    global delay
    for i in range(len(board)):
        for j in range(len(board[0])):
            nextBoard[i][j] = checkStatus(board,i,j)
    board = copy.deepcopy(nextBoard)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                color = "black"
            else:
                color = "white"
            canvas.itemconfig(cell_rectangles[i][j],fill=color)
    root.after(delay,start_simulation)

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

cell_rectangles = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        cell_rectangles[i][j] = canvas.create_rectangle(
            j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="white"
        )

canvas.bind("<Button-1>", on_cell_click)

control_frame = tk.Frame(root)
control_frame.pack()

start_button = tk.Button(control_frame, text="Start", command=start_simulation)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(control_frame, text="Stop", command=exit)
stop_button.pack(side=tk.LEFT, padx=5)

delay = 1

root.mainloop()
