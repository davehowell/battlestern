#!/usr/bin/env python3
"""
2 players, 4 boards
This is Object Oriented AF

does a board have player or a player has boards?
1 player has a relationship with 2 boards and 1:N hierachies make more sense...
do they? Otherwise 1 player belongs to 2 boards which is strange

"""

# placement board + tracking board for player 1 & player 2
# attack the tracking board, which attacks the opponent placement board
# player1 tracking board calls player 2's placement board.

# placement board is a "fleet", a minimal set of 
# the ship instances, 
# and a lightweight datastructure for hits/misses
# and remaining ships


# Store fleet placement
# Easily retrieve status of ships
# Easily retrieve ship coordinates
# Pass in missile strike, store if hit, return boolean hit
# Attack the tracking board, p

from itertools import product
from pprint import pprint

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.exceptions import BoardError

class Board(object):

    def __init__(self):
        self.coords = self.new_board()


    def new_board(self):
        """
        Board stores the state of the game, hits and misses for missile strikes,
        where a coordinates as a dictionary (hash map).

        Uses tuples of coordinates (col, row) as the dictionary keys.
        Initial values of None (Unknown state), are replaced with 'hit' or 'miss'
        If this were larger it could be generated lazily but it's trivial to create eagerly.
        A list of cols are rows are combined using a cartestian product function that 
        is effectively a memory optimised nested loop (uses generators).        
        """
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coords = {(col, row):None for (col, row) in product(cols, rows)}
        return coords

def main():
    b = Board()

    print(type( b.coords))
    pprint(b.coords)
    #for k, v  in b.coords:
    #    print(k)
    #    print(v)        

if __name__ == '__main__':
    main()