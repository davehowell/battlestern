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




class Board(object):
    pass

class PlayerBoard(Board):
    def __init__(self,
        player):
        self.player = player

class OpponentBoard(Board):
    pass

