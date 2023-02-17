from abc import ABC, abstractmethod
from typing import Iterable, TYPE_CHECKING, Dict, Type, Callable

from game.exceptions import MissingComponentError

if TYPE_CHECKING:
    from game.components import ComponentType, ComponentState
    from game.context import GameContext
    from game.events import Event
    from game.objects import GameObject


class Component(ABC):
    dependencies: Iterable['ComponentType'] = []

    def __init__(self, owner: 'GameObject'):
        self._owner = owner
        self._probe()

    @property
    @abstractmethod
    def type(self) -> 'ComponentType':
        pass

    @abstractmethod
    def get_state(self) -> 'ComponentState':
        pass

    def process_event(self, event: 'Event', context: 'GameContext'):
        handler = self._event_handlers.get(type(event))
        if handler:
            handler(event, context)

    @property
    def _event_handlers(self) -> Dict[Type, Callable]:
        return {}

    def _probe(self):
        for component_type in self.dependencies:
            if not self._owner.has_component(component_type):
                raise MissingComponentError(f'Required component {component_type} not found')
