from abc import ABC
from collections import deque
from typing import List, Optional
from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from .object_state import ObjectState

if TYPE_CHECKING:
    from game.context import GameContext
    from game.components import Component
    from game.events import Event


class GameObject(ABC):
    def __init__(self, components: Optional[List['Component']] = None, tag: str = ''):
        self._id = uuid4()
        self._components: List['Component'] = components or []
        self._events = deque()
        self._tag = tag

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def tag(self) -> str:
        return self._tag

    def get_state(self) -> ObjectState:
        return ObjectState(
            object_id=self.id,
            tag=self.tag,
            components=[component.get_state() for component in self._components],
        )

    def has_component(self, component_type: str) -> bool:
        return any(c.type == component_type for c in self._components)

    def send_event(self, event: 'Event'):
        self._events.append(event)

    def process_events(self, context: 'GameContext'):
        while self._events:
            event = self._events.popleft()
            for component in self._components:
                component.process_event(event, context)
