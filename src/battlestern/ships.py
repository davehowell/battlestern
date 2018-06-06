#!/usr/bin/env python3

from typing import Set, Tuple, Dict, List, Union, Mapping
from pprint import pprint
import random
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from battlestern.coordinates import Coordinate
from battlestern.exceptions import OrientationError, CoordinateError

    This, along with the orientation and the length of a ship
    uniquely define its placement on the board


class Ship(object):
    """
    A super class for the different types of ships

    :param length: Number of occupied horizontal or vertical contiguous coordinates
    :type length: int between 1 and 5
    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.
    """
    orientations = ['horizontal', 'vertical']

    def __init__(self,
                 length: int,
                 orientation: str,
                 bow_coordinate: Mapping[str, Union[str, int]] ,
                 **kwargs) -> None:
        self.length = length
        if orientation in self.orientations:
            self.orientation = orientation
        else:
            raise OrientationError(
                'orientation must be one of {}'
                .format(', '.join(self.orientations)))

        if isinstance(bow_coordinate, Coordinate):
            self.bow_coordinate = bow_coordinate
        else:
            raise CoordinateError(
                'Ship bow_coordinate must be of type Coordinate'
            )

class Carrier(Ship):
    """
    The largest type of ship
    Most likely to be hit but can take the most hits so is resilient

    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string

    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.
    """
    def __init__(self, **kwargs):
        super().__init__(length=5, **kwargs)
        self.name = 'carrienr'

class Battleship(Ship):
    """
    The second largest type of ship

    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.
    """
    def __init__(self, **kwargs):
        super().__init__(length = 4, **kwargs)
        self.name = 'battleship'

class Submarine(Ship):
    """
    A medium sized ship

    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.    
    """
    def __init__(self, **kwargs):
        super().__init__(length = 3, **kwargs)
        self.name = 'submarine'

class Cruiser(Ship):
    """
    The second smallest ship

    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.    
    """
    def __init__(self, **kwargs):
        super().__init__(length = 2, **kwargs)
        self.name = 'cruiser'

class Patrol(Ship):
    """
    The smallest ship
    Least likely to be hit
    Also the most vulnerable as a direct hit will sink it

    :param orientation: The way a ship is lying in the coordinates of the board
        either `horizontal` or `vertical`
    :type orientation: string
    :param bow_coordinate: The coordinates on the board for the bow of the ship
    :type bow_coordinate: An instance of battlestern.coordinates.Coordinate
        or a Mapping/dict-like object with `col` and `row` keys.    
    """
    def __init__(self, **kwargs):
        super().__init__(length = 1, **kwargs)
        self.name = 'patrol'

class Fleet(object):
    """
    A Fleet is a group of ships.
    The shipyard contains a mapping from lowercase name
    to ship classes.

    :param fleetroster: A set of ships and positional properties, 
        bow_coordinates & orientation
    :type fleetroster: A dictionary (JSON-like) or None
        In this format:
        { 'carrier': { col: 'a', row: 1, orientation: 'horizontal'}, ... }
        Keys must be one of carrier|battleship|submarine|cruiser|patrol
        col must a letter a through f
        row must be an integer 1 through 10
        orientation must be one of horizontal|vertical
    """

    shipyard: Dict[str, Ship] = {
                "carrier": Carrier,
                "battleship": Battleship,
                "submarine": Submarine, 
                "cruiser": Cruiser, 
                "patrol": Patrol }

    def __init__(self,
                 fleetroster: Mapping[str, Mapping[str, Union[str, int]]]) -> None:
        """
        Take a fleetroster or generate a random one, then create an armada.
        A fleetroster is effectively a JSON recipe for constructing an armada of ship objects,
        which have all their coordinates listed in full, and a way to track hits.
        """
        if fleetroster:
            self._fleetroster = fleetroster
        else:
            self._fleetroster = self._random_fleetroster()
        self._fleet = self._load_fleet(self._fleetroster)        
        self.armada = self._expand_fleet(self._fleet)
        self.duplicates, self.out_of_bounds = self.validate_coords(self.armada)

    def _load_fleet(self,
            fleetroster: Mapping[str, Mapping[str, Union[str, int]]] ) -> List[Ship]:
        """
        Parses a client-provided fleet roster and loads ship subclass instances to a list.

        :param fleetroster: A set of ships and positional properties, 
            bow_coordinates & orientation
        :type fleetroster: A dictionary (JSON-like) or None
            In this format:
            { 'carrier': { col: 'a', row: 1, orientation: 'horizontal'}, ... }
            Keys must be one of carrier|battleship|submarine|cruiser|patrol
            col must a letter a through f
            row must be an integer 1 through 10
            orientation must be one of horizontal|vertical
        
        Returns a list of battlestern.ships.Ship subclasses, one of each
        """
        loaded_fleet = []
        for ship, specs in fleetroster:
            ship = self.shipyard[ship.lower()]
            loaded_fleet.append(ship(orientation=specs['orientation'],
                 bow_coordinate=Coordinate(col=specs['col'],
                                              row=specs['row'])))
        return loaded_fleet

    def _random_fleetroster(self):
        """

        """
        fleetroster = {}
        for shipname, shiptype in Fleet.shipyard:
            orientation = random.choice(Ship.orientations)
            if orientation == 'horizontal':
                ringfence = len(Coordinate.allowedcols) - shiptype.length
                col = random.choice(Coordinate.allowedcols[0:ringfence])
                row = random.choice(Coordinate.allowedrows)
            else:
                ringfence = len(Coordinate.allowedrows) - shiptype.length
                col = random.choice(Coordinate.allowedcols)
                row = random.choice(Coordinate.allowedrows[0:ringfence])
            nose_coord = Coordinate(col=col, row=row)
            fleetroster.setdefault(shipname, 
                    {'col':nose_coord['col'], 'row':nose_coord['row'], 'orientation': orientation})
        return fleetroster

    def _expand_fleet(self, loaded_fleet: List[Ship]):
        """
        Takes bow_coordinates, orientation and length and expands
        to the full set of ship coordinate tuples.

        :param fleet: A loaded fleetroster, instances of all the ships.
        :type fleet: a List of battlestern.ships.Ship subclasses, one of each.

        Returns a battle-ready armada with all armour intact at all coordinates.
        A nested dictionary of ship subclass names for keys, pointing to values
        consisting of dictionaries using coordinates as keys and 'intact' or 'damaged'
        as values.

        The data structure is indexed by ship.name and coordinate, useful for checking 
        what coordinates a ship occupies it's O(1)
        It's not optimised for the other operation, checking if any ship 
        occupies a coordinate (i.e. seeing if a missle strike is a hit or miss) 
        and would suffer for very large fleets. 
        Luckily this game has 5 ships so the O(n) is trivial.
        """
        armada = {}
        for ship in loaded_fleet:
            if ship.orientation == 'horizontal':
                coords = ( (chr(ord(ship.bow_coordinate['col']) + i),
                            ship.bow_coordinate['row']) 
                            for i in range(ship.length) )
            else:
                coords = ( (ship.bow_coordinate['col'], 
                            ship.bow_coordinate['row'] + i) 
                            for i in range(ship.length) )
            armada[ship.name] = {(col, row): 'intact' for col, row in coords}
        return armada

    def validate_coords(self, 
                armada: Mapping[str, \
                            Mapping[Tuple[str, int], str]]) -> \
                                Union[Mapping[Tuple[str,int], List[str]], None]:
        """
        Finds duplicate coordinates, or those falling outside the grid 

        :param armada: An expanded fleet of ships & their coordinates
        :type armada: dict of ship.name : dict of Coord : Status
            Mapping[Tuple[str,int], List[str]]
        
        Returns duplicates and out_of_bounds dicts. 
            both are dict of coord:List[ships] or empty if validation successful
        
        This method intentionally doesn't raise an error as it would leave that
        to the client to determine.
        """
        coord_to_ships = {}
        #{('c', 4): ['battleship', 'submarine'], ...}
        # if ship has duplicate coords for battleship & submarine
        for ship, coords in armada.items():
            for coord in coords.keys():
                coord_to_ships.setdefault(coord, []).append(ship)
        duplicates = {coord: ships 
                      for coord, ships in coord_to_ships.items() 
                      if len(ships) > 1}
        out_of_bounds = {coord: ships 
                      for coord, ships in coord_to_ships.items() 
                      if coord[0] not in Coordinate.allowedcols
                      or coord[1] not in Coordinate.allowedrows}
        return duplicates, out_of_bounds


    def _strike(self, coordinates):
        """
        An attempted missile strike on a ship.
        Check if it hit a ship in the armada, if yes, mark it damaged at those coords
        and return a hit and random quote from the black knight,
        in the grand (Python) tradition of random Monty Python references.

        If a hit is the last coordinate of a ship to take damage it will return
        the special message 'You sunk my {shipname}!' e.g. if it was the battleship
        'You sunk my battleship!'
        
        This method should be called by the opponent's board, not directly.

        :param coordinates: Coordinates to land a missile strike on the opponent's fleet
        :type coordinates: Tuple[str, int]
        """
        hitmessages = ["It's just a flesh wound!",
                        "'tis but a scratch",
                        "had worse",
                        "Right, I’ll do you for that",
                        "I'm invincible!",
                        "All right, we'll call it a draw.",
                        "Come back here and take what's coming to ya!",
                        "I'll bite your legs off!"
                        ]

        msg = 'You missed'
        for ship, coords in self.armada.items():
            for coord in coords.keys():
                if coordinates == coord:
                    self.armada[ship][coord] = 'damaged'
                    msg = f'You sank my {ship.name} !'
                    for damagereport in self.armada[ship].values():
                        if damagereport = 'intact'
                            msg = random.choice(hitmessages)
                    return 'hit', msg
        return 'miss' , msg
