from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Iterable, Optional, Set
from uuid import UUID

if TYPE_CHECKING:
    from game.objects.game_object import GameObject
    from game.scenes.map import Map


class Scene:
    def __init__(self, game_map: Optional['Map'] = None):
        self._objects: Dict[UUID, 'GameObject'] = dict()
        self._object_tags: Dict[str, Set[UUID]] = defaultdict(set)
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

    def get_objects_by_tag(self, tag: str) -> Iterable['GameObject']:
        """
        Get all object with specific tag.
        """
        object_ids = self._object_tags.get(tag, set())
        return (self._objects[object_id] for object_id in object_ids)

    def add_object(self, game_object: 'GameObject'):
        """
        Add object on the scenes.
        """
        self._objects[game_object.id] = game_object
        if game_object.tag:
            self._object_tags[game_object.tag].add(game_object.id)

    def remove_object(self, game_object: 'GameObject'):
        """
        Remove object from the scenes.
        """
        self._objects.pop(game_object.id)
        if game_object.tag:
            self._object_tags[game_object.tag].remove(game_object.id)
