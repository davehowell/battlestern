#!/usr/bin/env python3

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.exceptions import PlayerSetupError

class Player(object):
    """
    The should be exactly 2 players in this edition of battleship.
    Player1 & 2 are player objects initialized with names
    default values are not set here but can be managed by clients.
    Names can be updated without having to start a new game
    Players are composed together with a fleet and a board in a game.

    :param name: Player's name
    :type name: string
    :param number: Player's number
    :type number: int either 1 or 2
    """

    def __init__(self,
                 name: str ,
                 number: int) -> None:
        if name is None:
            raise PlayerSetupError("Players must be named")
        else:
            self._name: str = name
        if number not in [1,2]:
            raise PlayerSetupError("Player must be numbered 1 or 2")
        else:
            self._number: int = number

    @property
    def name(self):
        """
        A player's (re-assignable) name
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Only the Player.name property has a setter
        Other properties are immutable.
        """
        self._name = name

    @property
    def number(self):
        """
        A player's immutable number
        """
        return self._number
