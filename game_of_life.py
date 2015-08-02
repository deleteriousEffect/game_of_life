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
        for cell in range(0, size):
            if should_live(board, row, cell):
                new_board[row][cell] = live_cell

            if should_die(board, row, cell):
                    new_board[row][cell] = dead_cell
    return new_board

def count_neighbors(board, row, cell):
    count = 0
    size = len(board)
    directions_to_surrounding_cells = list(product(*[[-1,0,1],[-1, 0, 1]]))
    # Remove directions to current cell
    directions_to_surrounding_cells.remove((0,0))
    for direction in directions_to_surrounding_cells:
        if is_alive(board,
                    row + direction[0],
                    cell + direction[1]):
            count += 1
    return count

# Check to see if a cell is alive.
def is_alive(board, row, cell):
    size = len(board)
    return (board
    [wrap_cells(row, size)]
    [wrap_cells(cell, size)]
    == live_cell)

def should_live(board, row, cell):
    num_neighbors = count_neighbors(board, row, cell)
    # Any live Cell with two or three neighbors lives on
    if is_alive(board, row, cell):
        return (2 <= num_neighbors <= 3)

    # Any dead cell with exactly three neighbors becomes alive
    if not is_alive(board, row, cell):
        return (num_neighbors == 3)

def should_die(board, row, cell):
    num_neighbors = count_neighbors(board, row, cell)

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
