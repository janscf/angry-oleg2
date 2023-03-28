from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.objects.game_object import GameObject
    from game.scenes import Scene


class Spawner(ABC):
    @abstractmethod
    def spawn(self, scene: 'Scene') -> 'GameObject':
        pass
