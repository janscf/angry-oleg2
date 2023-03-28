from typing import TYPE_CHECKING

from action_type import ActionType
from commands.move_command import MoveCommand
from game.components import Component, ComponentState
from game.components.decorators import event_handler
from game.events.time_passed_event import TimePassedEvent
from game.scenes.map import Direction
from ui.input import Input


if TYPE_CHECKING:
    from game.context import GameContext
    from game.objects import GameObject


class UserInput(Component):
    """Component responsible for user input"""

    def __init__(self, owner: 'GameObject'):
        super().__init__(owner)
        self._command_binding = {
            ActionType.MoveNorth: MoveCommand(receiver=owner, direction=Direction.North),
            ActionType.MoveEast: MoveCommand(receiver=owner, direction=Direction.East),
            ActionType.MoveSouth: MoveCommand(receiver=owner, direction=Direction.South),
            ActionType.MoveWest: MoveCommand(receiver=owner, direction=Direction.West),
        }

    def get_state(self) -> 'ComponentState':
        return ComponentState(component_type=self.type)

    @event_handler(TimePassedEvent)
    def _execute_commands(self, event: TimePassedEvent, context: 'GameContext'):
        command = self._command_binding.get(Input.action)
        if command:
            command.execute()
