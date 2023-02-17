from game.objects import GameObject, ObjectType


class Player(GameObject):
    @property
    def type(self) -> 'ObjectType':
        return ObjectType.Player
