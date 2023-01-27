from abc import ABC, abstractmethod
from typing import Iterable, TYPE_CHECKING

from game.exceptions import MissingComponentError

if TYPE_CHECKING:
    from game.components import ComponentType, ComponentState
    from game.context import GameContext
    from game.messages import Message
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
    def get_state(self, context: 'GameContext') -> 'ComponentState':
        pass

    def process_message(self, message: 'Message', context: 'GameContext'):
        pass

    def _probe(self):
        for component_type in self.dependencies:
            if not self._owner.has_component(component_type):
                raise MissingComponentError(f'Required component {component_type} not found')
