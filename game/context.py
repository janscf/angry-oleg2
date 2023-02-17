from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.objects import GameObject
    from game.scenes import Scene
    from game.scenes.map import Position


class GameContext:
    def __init__(self, scene: 'Scene'):
        self._scene = scene

    def find_object(self, game_object: 'GameObject') -> 'Position':
        return self._scene.map.find_object(object_id=game_object.id)

    def move_object(self, game_object: 'GameObject', new_position: 'Position'):
        return self._scene.map.place_object(object_id=game_object.id, position=new_position)
