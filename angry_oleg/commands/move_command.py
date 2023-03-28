from typing import TYPE_CHECKING, Any, Optional

from prefabs.events.move_event import MoveEvent

from .command import Command

if TYPE_CHECKING:
    from game.scenes.map import Direction
    from game.objects.game_object import GameObject


class MoveCommand(Command):
    def __init__(self, receiver: 'GameObject', direction: 'Direction'):
        super().__init__()
        self._direction = direction
        self._receiver = receiver

    def execute(self, parameter: Optional[Any] = None):
        self._receiver.send_event(MoveEvent(direction=self._direction))
