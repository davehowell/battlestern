#!/usr/bin/env python3

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.exceptions import PlayerSetupError

class Player(object):
    def __init__(self,
                 name,
                 number,
                 fleet):
        if name is None:
            raise PlayerSetupError("Players must be named")
        else:
            self._name = name
        if number not in [1,2]:
            raise PlayerSetupError("Player must be numbered 1 or 2")
        else:
            self._number = number
        self._fleet = fleet

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
    def fleet(self):
        return self._fleet

    @property
    def number(self):
        return self._number
