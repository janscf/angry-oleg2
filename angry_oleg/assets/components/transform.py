from dataclasses import dataclass
from typing import Callable, Type, Dict, TYPE_CHECKING

from game.components import Component, ComponentType, ComponentState
from angry_oleg.assets.events.move_event import MoveEvent
from game.events.time_passed_event import TimePassedEvent
from game.scenes.map import Position

if TYPE_CHECKING:
    from game.context import GameContext
    from game.objects import GameObject


@dataclass(frozen=True)
class TransformState(ComponentState):
    position: Position


class Transform(Component):
    """Component responsible for physical transformations"""

    def __init__(self, owner: 'GameObject'):
        super().__init__(owner)
        self._position = Position(0, 0)

    @property
    def type(self) -> 'ComponentType':
        return ComponentType.Transform

    def get_state(self) -> 'ComponentState':
        return TransformState(
            component_type=ComponentType.Transform,
            position=self._position,
        )

    @property
    def _get_event_handlers(self) -> Dict[Type, Callable]:
        return {
            TimePassedEvent: self._update_position,
            MoveEvent: self._move_in_direction,
        }

    def _move_in_direction(self, event: MoveEvent, context: 'GameContext'):
        position = context.find_object(self._owner)
        offset = event.direction.get_normalized_offset()
        new_position = position.increment(*offset)
        context.move_object(self._owner, new_position)

    def _update_position(self, context: 'GameContext'):
        self._position = context.find_object(self._owner)
