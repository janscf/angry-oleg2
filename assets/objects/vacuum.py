from game.objects import GameObject, ObjectType


class Vacuum(GameObject):
    @property
    def type(self) -> ObjectType:
        return ObjectType.Vacuum
