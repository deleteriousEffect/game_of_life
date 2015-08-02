# Load board from presets file
from time import sleep
from os import system
from copy import deepcopy

import presets

loaded_board = deepcopy(presets.toad)

live_cell = '#'
dead_cell = '_'
# Display board
def display_board(board):
    for row in board:
        print('')
        for cell in row:
            print(cell, end='')
    print('')

# Update board
def update_board(board):
    size = len(board)
    new_board = deepcopy(board)
    # Check every cell
    for row in range(0, size):
        for cell in range(0, size):
            num_neighbors = count_neighbors(board, row, cell)
        # If live
            if board[row][cell] == live_cell:
                # Any cell with fewer than two neighbors dies
                if num_neighbors < 2:
                    new_board[row][cell] = dead_cell
                # Any Cell with two or three neighbors lives on
                # Any Cell with more than three neighbors dies
                if num_neighbors > 3:
                    new_board[row][cell] = dead_cell
            # If dead
            if board[row][cell] == dead_cell:
                # Any dead Cell with exactly three neighbors becomes a live Cell
                if num_neighbors == 3:
                    new_board[row][cell] = live_cell
    return new_board

def count_neighbors(board, row, cell):
    count = 0
    size = len(board)
    # Look north
    if board[wrap_cells(row - 1, size)][cell] == live_cell:
        count += 1
    # Look northeast
    if board[wrap_cells(row - 1, size)][wrap_cells(cell + 1, size)] == live_cell:
        count += 1
    # Look northwest
    if board[wrap_cells(row - 1, size)][wrap_cells(cell - 1, size)] == live_cell:
        count += 1
    # Look west
    if board[row][wrap_cells(cell - 1, size)] == live_cell:
        count += 1
    # Look east
    if board[row][wrap_cells(cell + 1, size)] == live_cell:
        count += 1
    # Look south
    if board[wrap_cells(row + 1, size)][cell] == live_cell:
        count += 1
    # Look southeast
    if board[wrap_cells(row + 1, size)][wrap_cells(cell + 1, size)] == live_cell:
        count += 1
    # Look southwest
    if board[wrap_cells(row + 1, size)][wrap_cells(cell - 1, size)] == live_cell:
        count += 1
    return count

# Wrap cells around if out of bounds
def wrap_cells(coordinate, size):
    if coordinate < 0:
        coordinate = size - 1
    elif coordinate >= size:
        coordinate = 0
    return coordinate

# Loop every 300? miliseconds until interrupt
while True:
    display_board(loaded_board)
    loaded_board = update_board(loaded_board)
    sleep(.3)
    system('clear')
