from typing import TYPE_CHECKING

from game import Game, GameStatus
from game.objects.spawner import Spawner

from prefabs.objects.player import Player
from prefabs.scenes.context import MainContextProvider
from prefabs.scenes.test_scene import SimpleScene
from ui.console.console_view import ConsoleView
from ui.input import Input

if TYPE_CHECKING:
    from game.scenes import Scene


class PlayerSpaner(Spawner):
    def spawn(self, scene: 'Scene') -> Player:
        player = Player()
        object_id = player.id
        scene.add_object(player)
        scene.map.place_object_in_random_position(object_id)
        return player


def main():
    game = Game(context_provider=MainContextProvider(), player_spawner=PlayerSpaner())
    game.load_scene(SimpleScene())

    player_id = game.add_player()
    view = ConsoleView()

    game.start()
    while game.status == GameStatus.Running:
        game.update()
        state = game.get_state(player_id)
        view.render_state(state=state)
        Input.wait_for_user_input()


if __name__ == '__main__':
    main()
