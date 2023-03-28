from abc import ABC, abstractmethod
from collections import defaultdict
import inspect
from typing import Iterable, TYPE_CHECKING, Dict, Type, Callable

from game.exceptions import MissingComponentError
from .decorators import HANDLED_EVENTS_ATTR

if TYPE_CHECKING:
    from game.components import ComponentState
    from game.context import GameContext
    from game.events import Event
    from game.objects import GameObject


class Component(ABC):
    dependencies: Iterable[str] = []

    def __init__(self, owner: 'GameObject'):
        self._owner = owner
        self._probe()
        self._type = type(self).__name__
        self._event_handlers: Dict[Type, list] = self.__get_event_handlers()

    @property
    def type(self) -> str:
        return self._type

    @abstractmethod
    def get_state(self) -> 'ComponentState':
        pass

    def process_event(self, event: 'Event', context: 'GameContext'):
        handlers = self._event_handlers.get(type(event), [])
        for handler in handlers:
            handler(event, context)

    def _probe(self):
        for component_type in self.dependencies:
            if not self._owner.has_component(component_type):
                raise MissingComponentError(f'Required component {component_type} not found')

    def __get_event_handlers(self) -> Dict[Type, list]:
        handlers = defaultdict(list)
        for _, method in inspect.getmembers(self, inspect.ismethod):
            if hasattr(method, HANDLED_EVENTS_ATTR):
                for event_type in getattr(method, HANDLED_EVENTS_ATTR):
                    handlers[event_type].append(method)

        return handlers