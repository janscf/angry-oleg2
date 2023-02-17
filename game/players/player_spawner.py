from abc import ABC, abstractmethod
from copy import copy
from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from game.objects import GameObject
    from game.scenes import Scene


@dataclass(frozen=True)
class Player:
    player_id: UUID
    object_id: UUID


class PlayerSpawner(ABC):
    def __init__(self, player_prefab: 'GameObject'):
        self._player_prefab = player_prefab

    @abstractmethod
    def instantiate(self, scene: 'Scene') -> Player:
        pass


class RandomPositionSpawner(PlayerSpawner):
    def instantiate(self, scene: 'Scene') -> Player:
        player_object = copy(self._player_prefab)
        object_id = player_object.id
        scene.add_object(player_object)
        scene.map.place_object_in_random_position(object_id)

        return Player(player_id=uuid4(), object_id=object_id)
