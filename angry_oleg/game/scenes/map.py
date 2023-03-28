from dataclasses import dataclass
from enum import Enum
from math import sqrt
import random
from collections import defaultdict
from typing import Dict, Tuple
from typing import Iterable
from typing import List
from typing import Optional
from uuid import UUID

from game.exceptions import InvalidMapSizeError, OutOfMapError


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __str__(self):
        return f'{self.x}, {self.y}'

    def calc_distance(self, other_position: 'Position') -> float:
        return sqrt((self.x - other_position.x) ** 2 + (self.y - other_position.y) ** 2)

    def increment(self, dx: int, dy: int) -> 'Position':
        return Position(self.x + dx, self.y + dy)


class Direction(Enum):
    North = 'n'
    South = 's'
    West = 'w'
    East = 'e'
    NorthWest = 'nw'
    NorthEast = 'ne'
    SouthWest = 'sw'
    SouthEast = 'se'

    @staticmethod
    def from_offset(dx: int, dy: int) -> Optional['Direction']:
        if dx > 0 and dy > 0:
            return Direction.NorthEast
        elif dx > 0 > dy:
            return Direction.SouthEast
        elif dx < 0 < dy:
            return Direction.NorthWest
        elif dx < 0 and dy < 0:
            return Direction.SouthWest
        elif dx == 0 and dy > 0:
            return Direction.North
        elif dx == 0 and dy < 0:
            return Direction.South
        elif dx > 0 and dy == 0:
            return Direction.East
        elif dx < 0 and dy == 0:
            return Direction.West
        return None

    def get_normalized_offset(self) -> Tuple[int, int]:
        dx = 0
        dy = 0

        if self == Direction.North or self == Direction.NorthEast or self == Direction.NorthWest:
            dy = 1
        elif self == Direction.South or self == Direction.SouthEast or self == Direction.SouthWest:
            dy = -1
        if self == Direction.East or self == Direction.NorthEast or self == Direction.SouthEast:
            dx = 1
        elif self == Direction.West or self == Direction.NorthWest or self == Direction.SouthWest:
            dx = -1

        return dx, dy


class Map:
    def __init__(self, size_x: int, size_y: int):
        if size_x <= 0 or size_y <= 0:
            raise InvalidMapSizeError('World size must be greater than zero')

        self._size_x = size_x
        self._size_y = size_y

        self._map: Dict['Position', List] = defaultdict(list)
        self._reversed_map: Dict[UUID, 'Position'] = dict()

    @property
    def size_x(self) -> int:
        return self._size_x

    @property
    def size_y(self) -> int:
        return self._size_y

    def __getitem__(self, position: 'Position') -> Iterable[UUID]:
        """
        Get all object in the specified position.
        """
        return self._map.get(position, [])

    def find_object(self, object_id: UUID) -> Optional['Position']:
        """
        Find object position on the map by ID.
        """
        return self._reversed_map.get(object_id)

    def calc_distance(self, object_from_id: UUID, object_to_id: UUID) -> float:
        """
        Calculate distance between two players with the specified IDs.
        """
        position_from = self.find_object(object_from_id)
        position_to = self.find_object(object_to_id)
        return position_from.calc_distance(position_to)

    def get_direction(self, object_from_id: UUID, object_to_id: UUID) -> Direction:
        """
        Get a direction from one object to another.
        """
        position_from = self.find_object(object_from_id)
        position_to = self.find_object(object_to_id)
        delta_x = position_to.x - position_from.x
        delta_y = position_to.y - position_from.y
        return Direction.from_offset(delta_x, delta_y)

    def is_valid_position(self, position: 'Position') -> bool:
        """
        Check if the specified position is valid.
        """
        return self._size_x >= position.x > 0 and self._size_y >= position.y > 0

    def place_object(self, object_id: UUID, position: 'Position'):
        """
        Add a new object on the map in the specified position.
        """
        if not self.is_valid_position(position):
            raise OutOfMapError(f'Position {position} is out of map bounds')

        self.remove_object(object_id)
        self._map[position].append(object_id)
        self._reversed_map[object_id] = position

    def place_object_in_random_position(self, object_id: UUID):
        """
        Add a new object on the map in random position.
        """
        position = Position(
            x=random.randint(1, self.size_x),
            y=random.randint(1, self.size_y),
        )
        self.place_object(object_id, position)

    def remove_object(self, object_id: UUID):
        """
        Remove object from the map.
        """
        object_position = self.find_object(object_id)
        if object_position:
            self._reversed_map.pop(object_id)
            self._map[object_position].remove(object_id)
