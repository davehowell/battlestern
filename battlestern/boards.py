#!/user/bin/python3
"""
2 players, 4 boards
This is Object Oriented AF

does a board have player or a player has boards?
1 player has a relationship with 2 boards and 1:N hierachies make more sense...
do they? Otherwise 1 player belongs to 2 boards which is strange

API
Initialize player names
players have 2 boards each
keep track of player and opponent (not the player)
Random ship placements or
Manual ship placements

new_game(players, boards)

"""

class Board(object):
    pass

class PlayerBoard(Board):
    def __init__(self,
        player):
        self.playername = player

class OpponentBoard(Board):
    pass


class Player(object):
    def __init__(self,
    playername):
        self.playername = playername
