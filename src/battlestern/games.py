#!/usr/bin/env python3
"""
Game is the entrypoint for the battlestern API
Initializing a new game with battlestern requires:

player names
   defaults to Bob & Alice
   players have a board to track their strikes
   players have a fleet which evaluates & stores strikes from the opponent.
fleets
    Can be passed in as manual ship placements
    or default to random ship placements

e.g.
with no playernames or fleets provided:
game = Game()

You can change player names: 
game.player1.name = 'Eddy'

You can assign a player fleet game.player1.fleet = 'thing'
"""

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from .players import Player
from .boards import Board
from battlestern.ships import Fleet


class Game(object):
    def __init__(self,
                 player1name=None,
                 player2name=None,
                 player1fleet=None,
                 player2fleet=None):
 
        self._player1name = player1name
        if player1name is None:
            self._player1name = 'Bob'
        self._player2name = player2name
        if player2name is None:
            self._player2name = 'Alice'

        # Player names are public so shouldn't be the same value
        if self._player1name == self._player2name:
            self._player2name = self._player2name + '_1'

        self._player1 = Player(name=player1name,number=1)
        self._player2 = Player(name=player2name,number=2)

        # dynamic attributes - Poor man's dependency injection
        # Compose players with boards
        self._player1.board = Board()
        self._player2.board = Board()
        # Compose players with fleets
        self._player1.fleet = self.create_fleet(fleetroster=player1fleet)
        self._player2.fleet = self.create_fleet(fleetroster=player2fleet)

        # Compose player with opponent
        self._player1.opponent = self._player2
        self._player2.opponent = self._player1


    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2


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


    def strike(self, player, coord):
        result, message = player.opponent.fleet._strike(coord)
        player.board.mark_strike(coord=coord, result=result)

        return result, message