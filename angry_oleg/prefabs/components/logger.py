from dataclasses import dataclass
from typing import TYPE_CHECKING, Iterable

from game.components import Component, ComponentState
from game.components.decorators import event_handler
from game.events.time_passed_event import TimePassedEvent
from game.scenes.map import Position

from prefabs.events.move_event import MoveEvent

if TYPE_CHECKING:
    from game.context import GameContext
    from game.objects import GameObject


@dataclass(frozen=True)
class LoggerState(ComponentState):
    messages: Iterable[str]


class Logger(Component):
    """Component responsible for collecting of events occurred"""

    def __init__(self, owner: 'GameObject'):
        super().__init__(owner)
        self._events = []

    def get_state(self) -> 'ComponentState':
        return LoggerState(
            component_type=self.type,
            messages=self._events,
        )

    @event_handler(MoveEvent)
    def _move_in_direction(self, event: MoveEvent, context: 'GameContext'):
        position = context.find_object(self._owner)
        offset = event.direction.get_normalized_offset()
        new_position = position.increment(*offset)

        context.move_object(self._owner, new_position)
        self._position = new_position

    @event_handler(TimePassedEvent)
    def _update_position(self, event: TimePassedEvent, context: 'GameContext'):
        self._position = context.find_object(self._owner)
