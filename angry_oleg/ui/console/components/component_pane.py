from typing import TYPE_CHECKING, Generic, TypeVar

from rich.panel import Panel


if TYPE_CHECKING:
    from game import GameState


T = TypeVar('T')

class ComponentPane(Generic[T]):
    def __init__(self, component_state: T, game_state: 'GameState'):
        self._component = component_state
        self._game = game_state

    def render(self):
        return Panel(str(self))
