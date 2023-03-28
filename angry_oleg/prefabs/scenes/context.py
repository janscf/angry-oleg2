from typing import TYPE_CHECKING
from game.scenes.context import ContextProvider, GameContext

if TYPE_CHECKING:
    from game.objects import GameObject
    from game.scenes import Scene
    from game.scenes.map import Position


class MainContext(GameContext):
    def find_object(self, game_object: 'GameObject') -> 'Position':
        return self._scene.map.find_object(object_id=game_object.id)

    def move_object(self, game_object: 'GameObject', new_position: 'Position'):
        if self._scene.map.is_valid_position(position=new_position):
            self._scene.map.place_object(object_id=game_object.id, position=new_position)


class MainContextProvider(ContextProvider):
    def get_context(self, scene: 'Scene') -> GameContext:
        return MainContext(scene=scene)
