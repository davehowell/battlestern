#!/usr/bin/env python3


import sys
from os import path
from collections.abc import Mapping
from typing import List
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.exceptions import CoordinateError

class Coordinate(Mapping):
    """
    The coordinates of a ship or on a board.

    :param col: A valid column reference on the board
    :type col: string, one of the letters from a to j
    :param row: A valid row reference on the board
    :type row: int, between 1 and 10
    """

    allowedkeys: List[str] = ['col', 'row']
    allowedcols: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    allowedrows: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, *args, **kwargs: str) -> None:
        """

        """
        keyset = set(self.allowedkeys)
        colset = set(self.allowedcols)
        rowset = set(self.allowedrows)
        if kwargs.keys() & keyset != keyset:
            raise CoordinateError(
                'Coordinates can only have a `col` and a `row` not these: {}'
                .format(', '.join(kwargs.keys()))
                )
        if kwargs.get('col') not in colset:
            raise CoordinateError(
                'col must be one of {}'
                .format(','.join(colset))
                )
        if kwargs.get('row') not in rowset:
            raise CoordinateError(
                'row must be one of {}'
                .format(','.join(rowset))
                )
        self._storage = dict(*args, **kwargs)

    def __getitem__(self, key):
        if key not in ['col', 'row']:
            raise CoordinateError(
                'Coordinates only have a `col` and a `row`')
        return self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)