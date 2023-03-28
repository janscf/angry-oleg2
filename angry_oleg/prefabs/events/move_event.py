from typing import TYPE_CHECKING

from game.events.event import Event

if TYPE_CHECKING:
    from game.scenes.map import Direction


class MoveEvent(Event):
    def __init__(self, direction: 'Direction'):
        self._direction = direction

    @property
    def direction(self) -> 'Direction':
        return self._direction
