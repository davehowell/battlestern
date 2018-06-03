#!/usr/bin/env python3
"""
A game initializes and then needs

player names, default human & computer
   players have a board to track their strikes
   and a fleet

Random ship placements or
Manual ship placements

keep track of player and opponent (not the player)
new_game(players, boards)

"""

from battlestern.boards import Board
from battlestern.players import Player

# players?

# game = Game()
#You can change player names: game.player1.name = 'Eddy'
#You can assign a player fleet game.player1.fleet = 'thing'

class Game(object):
    def __init__(self,
                 player1name=None,
                 player2name=None,
                 player1fleet=None,
                 player2fleet=None):
        #gameid?

        # PLAYER NAMES - mutable
        self._player1name = player1name
        if player1name is None:
            self._player1name = 'Bob'
        self._player2name = player2name
        if player2name is None:
            self._player2name = 'Alice'

        # FLEETS - Provided or Random - immutable
        self._player1fleet = create_fleet(fleet=player1fleet)
        self._player2fleet = create_fleet(fleet=player2fleet)

        self._player1 = Player(player1name, player1fleet)
        self._player2 = Player(player2name, player2fleet)

# player1 & 2 are objects initialized with names
# can use default names
# names can be updated
# players have a fleet and a board
# fleet can either be set up & provided
# or if not passed in will be generated with random placement
# boards & fleets cannot be altered. Need to start a new game.

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, player1):
        self._player1 = player1

    @property
    def player2(self):
        return self._player2

    @player2.setter
    def player2(self, player2):
        self._player2 = player2

    @property
    def player1fleet(self):
        return self._player1fleet

    @property
    def player2fleet(self):
        return self._player2fleet


    def create_fleet(self, fleet):
        if fleet is None:
            # ships.random_fleet() ?
        else:
            # ships.specified_fleet()


    def get_opponent(self, playername):
        if playername == self.player1.name:
            return self.player2
        else:
            return self.player1

