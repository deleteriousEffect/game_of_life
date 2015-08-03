from time import sleep
from os import system
from copy import deepcopy
from itertools import product
import sys
import argparse

# Load boards from presets file
import presets


# Appearance of live and dead cells
live_cell = '#'
dead_cell = ' '

# Take the name of a pattern as a command-line argument.
parser = argparse.ArgumentParser(description = 'Process arguments for game of life')
parser.add_argument('--pattern',
                    type=str.lower,
                    default='pentadecathlon',
                    choices = [item for item in dir(presets) if not item.startswith('__')])
args = parser.parse_args()

print(args.pattern)
user_preset = args.pattern

def get_pattern(pattern):
        path_to_preset = eval('presets.' + pattern)
        return deepcopy(path_to_preset)

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
    # Check every cell to see if it should be alive or dead
    # on the next iteration.
    for row in range(0, size):
        for column in range(0, size):
            if should_live(board, row, column):
                new_board[row][column] = live_cell

            if should_die(board, row, column):
                    new_board[row][column] = dead_cell
    return new_board

def count_neighbors(board, row, column):
    count = 0
    size = len(board)
    neighboring_cell_offsets = list(product(*[[-1,0,1],[-1, 0, 1]]))
    # Remove directions to current cell
    neighboring_cell_offsets.remove((0,0))
    for offsets in neighboring_cell_offsets:
        vertical_offset, horizontal_offset = offsets
        if is_alive(board,
                    row + vertical_offset,
                    column + horizontal_offset):
            count += 1
    return count

# Check to see if a cell is alive.
def is_alive(board, row, column):
    size = len(board)
    return (board
    [wrap_cells(row, size)]
    [wrap_cells(column, size)]
    == live_cell)

def should_live(board, row, column):
    num_neighbors = count_neighbors(board, row, column)
    # Any live Cell with two or three neighbors lives on
    if is_alive(board, row, column):
        return (2 <= num_neighbors <= 3)

    # Any dead cell with exactly three neighbors becomes alive
    if not is_alive(board, row, column):
        return (num_neighbors == 3)

def should_die(board, row, column):
    num_neighbors = count_neighbors(board, row, column)

    # Any cell with fewer than two neighbors dies
    # Any Cell with more than three neighbors dies
    return (num_neighbors > 3 or num_neighbors < 2)


# Wrap cells around if out of bounds
def wrap_cells(coordinate, size):
    if coordinate < 0:
        coordinate = size - 1
    elif coordinate >= size:
        coordinate = 0
    return coordinate

def start_game(loaded_board):
    # Loop every 300? miliseconds until interrupt
    while True:
        display_board(loaded_board)
        loaded_board = update_board(loaded_board)
        sleep(.3)
        system('clear')

board = get_pattern(user_preset)
start_game(board)
