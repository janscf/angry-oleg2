from typing import TYPE_CHECKING

from rich import print
from rich.console import Console

from ui import View
from ui.console.components.factory import create_component_pane

if TYPE_CHECKING:
    from game.game import GameState


class ConsoleView(View):
    def render_state(self, state: 'GameState'):
        player_state = state.objects[state.player.object_id]

        console = Console()
        console.clear()
        for component in player_state.components:
             pane = create_component_pane(component, state)
             if pane:
                print(pane)
