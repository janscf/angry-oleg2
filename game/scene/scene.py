from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Set
from uuid import UUID

if TYPE_CHECKING:
    from game.objects.game_object import GameObject, ObjectType


class Scene:
    def __init__(self):
        self.__objects: Dict[UUID, 'GameObject'] = dict()
        self.__object_types: Dict['ObjectType', Set[UUID]] = defaultdict(set)

    def get_object(self, object_id: UUID) -> Optional['GameObject']:
        '''
        Game object by ID.
        '''
        return self.__objects.get(object_id)

    def get_all_objects(self) -> Iterable['GameObject']:
        '''
        Get all objects.
        '''
        return list(self.__objects.values())

    def get_objects_by_type(self, object_type: 'ObjectType') -> Iterable['GameObject']:
        '''
        Get all object of specific type.
        '''
        object_ids = self.__object_types.get(object_type, set())
        return [self.__objects[object_id] for object_id in object_ids]

    def add_object(self, game_object: 'GameObject'):
        '''
        Add object on the scene.
        '''
        self.__objects[game_object.id] = game_object
        self.__object_types[game_object.type].add(game_object.id)
