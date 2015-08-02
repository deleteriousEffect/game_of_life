#Conway's game of life in python 3

This a simple command-line version of [Conway's Game of Life](Conway's_Game_of_Life).

Conway's Game of Life uses simple rules to that allows complex patterns to be generated based on the placement of cells.

The rules (from Wikipedia) are:

    1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overcrowding.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                

##Requirements:
  * Linux
  * Python 3

##How to install
  1. Clone the repository [link](https://github.com/haySwim/game_of_life.git)

##How to use
  1. Start a terminal
  2. Move into the directory where you cloned the repository
  3. type `python game_of_life.py`
  4. (optional) to see different patterns, use the --pattern option
    * i.e., `python game_of_life.py --pattern=toad`

##Available patterns
  * toad: It looks like a jumping toad... kinda
  * blinker: It blinks
  * glider: Super fun, iconic Game of Life pattern, files across the terminal
  * lwss: Lightweight Spaceship, majestically floats sideways
  * pentadecathlon(default): Lots of permutations from this one, mercifully made the default you don't have to spell it
