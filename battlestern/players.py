#!/usr/bin/env python3

from battlestern import ships

class Player(object):
    def __init__(self,
                 name,
                 fleet):
        self._name = name
        self._fleet = fleet

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def fleet(self):
        return self._fleet
    
    @fleet.setter
    def fleet(self, fleet):
        self._fleet = fleet