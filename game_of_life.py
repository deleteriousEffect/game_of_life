# Load board from presets file
from time import sleep
from os import system
from copy import deepcopy
from itertools import product

import presets

loaded_board = deepcopy(presets.blinker)

live_cell = '#'
dead_cell = ' '
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
    directions = list(product(*[[-1,0,1],[-1, 0, 1]]))
    directions.remove((0,0))
    for direction_change in directions:
        if is_alive(board,
                    row + direction_change[0],
                    cell + direction_change[1]):
            count += 1
    return count

# Check to see if a cell is alive.
def is_alive(board, row, cell):
    size = len(board)
    return (board
    [wrap_cells(row, size)]
    [wrap_cells(cell, size)]
    == live_cell)

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
