from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Iterable, Optional, Set
from uuid import UUID

if TYPE_CHECKING:
    from game.objects.game_object import GameObject, ObjectType
    from game.scenes.map import Map


class Scene:
    def __init__(self, game_map: Optional['Map'] = None):
        self._objects: Dict[UUID, 'GameObject'] = dict()
        self._object_types: Dict['ObjectType', Set[UUID]] = defaultdict(set)
        self._map = game_map

    @property
    def map(self) -> 'Map':
        return self._map

    def get_object(self, object_id: UUID) -> Optional['GameObject']:
        """
        Game object by ID.
        """
        return self._objects.get(object_id)

    def get_all_objects(self) -> Iterable['GameObject']:
        """
        Get all players.
        """
        return (obj for obj in self._objects.values())

    def get_objects_by_type(self, object_type: 'ObjectType') -> Iterable['GameObject']:
        """
        Get all object of specific type.
        """
        object_ids = self._object_types.get(object_type, set())
        return (self._objects[object_id] for object_id in object_ids)

    def add_object(self, game_object: 'GameObject'):
        """
        Add object on the scenes.
        """
        self._objects[game_object.id] = game_object
        self._object_types[game_object.type].add(game_object.id)

    def remove_object(self, game_object: 'GameObject'):
        """
        Remove object from the scenes.
        """
        self._objects.pop(game_object.id)
        self._object_types[game_object.type].remove(game_object.id)
