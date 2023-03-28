from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.scenes.scene import Scene


class GameContext:
    def __init__(self, scene: 'Scene'):
        self._scene = scene


class ContextProvider(ABC):
    @abstractmethod
    def get_context(self, scene: 'Scene') -> GameContext:
        pass
