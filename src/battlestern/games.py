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
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from .boards import Board
from .players import Player
from .ships import Fleet

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


        self._player1fleet = create_fleet(fleetroster=player1fleet)
        self._player2fleet = create_fleet(fleetroster=player2fleet)

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
        """
        Player fleets are immutable
        """
        return self._player1fleet

    @property
    def player2fleet(self):
        """
        Player fleets are immutable
        """
        return self._player2fleet


    def create_fleet(self, fleetroster):
        """
        Created from a specified ship layout, or if None will be generated.

        :param fleetroster: A set of ships and positional properties, 
            bow_coordinates & orientation
        :type fleetroster: A dictionary (JSON-like) or None
            In this format:
            { 'carrier': { col: 'a', row: 1, orientation: 'horizontal'}, ... }
            Keys must be one of carrier|battleship|submarine|cruiser|patrol
            col must a letter a through f
            row must be an integer 1 through 10
            orientation must be one of horizontal|vertical
        
        Returns a new battlestern.ships.Fleet instance
        """
        return Fleet(fleetroster=fleetroster)

    
    def get_opponent(self, playername):
        if playername == self.player1.name:
            return self.player2
        else:
            return self.player1

