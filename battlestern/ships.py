#!/user/bin/python3

from collections.abc import Mapping
from .exceptions import OrientationError, CoordinateError

class BowCoordinate(Mapping):
    """
    The coordinates of the bow of a ship.
    This, along with the orientation and the length of a ship
    uniquely define its placement on the board

    :param column: A valid column reference on the board
    :type column: string, one of the letters from a to j
    :param row: A valid row reference on the board
    :type row: int, between 1 and 10
    """

    allowedkeys = {'column', 'row'}
    allowedcolumns = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    allowedrows = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    def __init__(self, *args, **kwargs):
        if kwargs.keys() & self.allowedkeys is not self.allowedkeys:
            raise CoordinateError(
                'Coordinates can only have a `column` and a `row`')
        if kwargs.get('column') not in self.allowedcolumns:
            raise CoordinateError(
                'column must be one of {}'
                .format(','.join(self.allowedcolumns))
                )
        if kwargs.get('row') not in self.allowedrows:
            raise CoordinateError(
                'row must be one of {}'
                .format(','.join(self.allowedrows))
                )
        self._storage = dict(*args, **kwargs)

    def __getitem__(self, key):
        if key not in ['column', 'row']:
            raise CoordinateError(
                'Coordinates only have a `column` and a `row`')
        return self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

class Ship(object):
    """
    A super class for the different types of ships in battleship

    :param orientation: The way a ship is lying in the coordinates of the board
        either horizontal or vertical
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.ship.BowCoordinate
        a dictionary-like object with `column` and `row` keys.

    """
    orientations = ['horizontal', 'vertical']

    def __init__(self,
                 length,
                 orientation,
                 bow_coordinate,
                 **kwargs):
        self.length = length
        if orientation in self.orientations:
            self.orientation = orientation
        else:
            raise OrientationError(
                'orientation must be one of {}'
                .format(', '.join(self.orientations)))

        if isinstance(bow_coordinate, BowCoordinate):
            self.bow_coordinate = bow_coordinate
        else:
            raise CoordinateError(
                'bow_coordinate must be an instance of BowCoordinate'
            )

class Carrier(Ship):
    """
    The largest type of ship
    Most likely to be hit but can take the most hits so is resilient
    """
    def __init__(self, **kwargs):
        super().__init__(length=5, **kwargs)

class Battleship(Ship):
    """
    The second largest type of ship
    """
    def __init__(self, **kwargs):
        super().__init__(length = 4, **kwargs)

class Submarine(Ship):
    """
    A medium sized ship
    """
    def __init__(self, **kwargs):
        super().__init__(length = 3, **kwargs)

class Cruiser(Ship):
    """
    The second smallest ship
    """
    def __init__(self, **kwargs):
        super().__init__(length = 2, **kwargs)

class Patrol(Ship):
    """
    The smallest ship
    Least likely to be hit
    Also the most vulnerable as a direct hit will sink it
    """
    def __init__(self, **kwargs):
        super().__init__(length = 1, **kwargs)

class Fleet(object):
    def __init__(self,
                 carrier,
                 battleship,
                 submarine,
                 cruiser,
                 patrol):
        self.carrier = carrier,
        self.battleship = battleship,
        self.submarine = submarine,
        self.cruiser = cruiser,
        self.patrol = patrol

# accept a ship setup (will be validated)
# { 'carrier': { row: 1, col: 'a', orientation: 'horizontal'}, ... }


# or generate a random one with no overlap
# sequential random, check overlap of previous
# e.g. 
# place carrier. 
#   1. rand horizontal or vertical.
#   2. if h, nosecoord rand row(1-10) and rand col between a and (j - ascii(length=5))
#   3. bag it
# place battleship (and the rest, probably generalize carrier to this as well)
#  1. same h/v
#  2. same nosecoord
#  3. check for collision with already placed ships in the bag
#  4. if collision, start at 1 again
#  5. else bag it
# place rest of ships

    # if ship.orientation = 'horizontal' then $col, row for row -> length 
    # else  col, $row for col => length ( bin(ascii(col) + i )) some ascii & back conversion?
# for ship in fleet, get coord, 
# if True set false & return hit
{ 'carrier' : { ('a', 1): True,
                ('a', 2): True,
                ('a', 3): True,
                ('a', 4): True,
                ('a', 5): True }


    def strike(self,coords):
