from typing import TYPE_CHECKING

from .transform_pane import TransformPane


if TYPE_CHECKING:
    from game import GameState
    from game.components.component_state import ComponentState
    from ui.console.components import ComponentPane



def create_component_pane(component: 'ComponentState', game_state: 'GameState') -> 'ComponentPane':
    mapping = {
        'Transform': TransformPane
    }
    if component.component_type not in mapping:
        return None

    return mapping[component.component_type](component, game_state)
