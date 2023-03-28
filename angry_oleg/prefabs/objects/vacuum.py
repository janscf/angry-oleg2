from game.objects import GameObject


class Vacuum(GameObject):
    def __init__(self):
        super().__init__(tag='vacuum')
