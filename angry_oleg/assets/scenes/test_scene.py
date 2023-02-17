from game.scenes import Scene
from game.scenes.map import Map


class SimpleScene(Scene):
    def __init__(self):
        super().__init__(game_map=Map(size_x=100, size_y=100))
