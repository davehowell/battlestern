#!/usr/bin/env python3
"""
A board is a mapping of coordinate tuples to state
Initialized as None, then marked with hit or miss

"""

# attack the player's tracking board, which attacks the opponent's Fleet

# placement board is a "fleet", a set of 
# the ship instances, 
# and a lightweight datastructure for hits/misses
# and remaining ships


# Pass in missile strike, store if hit, return 'hit' or 'miss'


from itertools import product
from pprint import pprint

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.exceptions import BoardError

class Board(object):

    def __init__(self):
        self.coords = self.new_coords()

    def new_coords(self):
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

    def get_coord(self, coord):
        return self.coords[coord]

    def mark_strike(self, coord, result):
        current_state =  self.get_coord(coord) 
        if current_state is not None:
            return 'Dejavu' # Hey if you waste a shot on the same coords too bad
        else:
            self.coords[coord] = result
            return None

