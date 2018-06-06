#!/usr/bin/env python3
""" 
tests for battlestern.players 

Usage
Run this suite only
python -m unittest tests/test_player.py

Test Discovery
python -m unittest
"""
import os
import sys
from unittest import TestCase, main

sys.path.insert(0, os.path.abspath('.'))

from src.battlestern.players import Player
from src.battlestern.exceptions import PlayerSetupError

class PlayersTestCase(TestCase):
    def setUp(self):
        pass

    def test_player_no_name(self):
        self.assertRaises(PlayerSetupError, Player(name=None, number=1) )

    def test_player_number(self):
        self.assertIsInstance(Player(name='George', number=1), Player )
    
    def test_player_invalid_number(self):
        self.assertRaises(PlayerSetupError, Player(name='Brian', number=3) )

    def tearDown(self):
        pass