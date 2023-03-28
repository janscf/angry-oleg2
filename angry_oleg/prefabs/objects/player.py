from prefabs.components import Transform, UserInput
from game.objects import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__(
            components=[
                UserInput(owner=self),
                Transform(owner=self),
            ],
            tag='player',
        )
