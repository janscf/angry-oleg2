from angry_oleg.assets.prefabs.player import Player
from angry_oleg.assets.scenes.test_scene import SimpleScene
from game import Game, GameStatus
from game.players.player_spawner import RandomPositionSpawner


def main():
    game = Game(player_spawner=RandomPositionSpawner(player_prefab=Player()))
    game.load_scene(SimpleScene())
    game.start()

    player_id = game.add_player()

    while game.status == GameStatus.Running:
        game.update()
        state = game.get_state()
        print(state)


if __name__ == '__main__':
    main()
