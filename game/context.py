from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.scene import Scene


class GameContext:
    def __init__(self, scene: 'Scene'):
        self.__scene = scene
