from abc import ABC
from abc import abstractmethod
from collections import deque
from typing import List
from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from .object_state import ObjectState

if TYPE_CHECKING:
    from game.context import GameContext
    from game.components import Component, ComponentType
    from game.messages import Message
    from game.objects import ObjectType


class GameObject(ABC):
    def __init__(self):
        self.__id = uuid4()
        self._components: List['Component'] = []
        self._messages = deque()

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def get_state(self) -> ObjectState:
        return ObjectState(
            object_id=self.id,
            object_type=self.type,
            components=[component.get_state() for component in self._components],
        )

    @property
    @abstractmethod
    def type(self) -> 'ObjectType':
        pass

    def has_component(self, component_type: 'ComponentType') -> bool:
        return any(c.type == component_type for c in self._components)

    def send_message(self, message: 'Message'):
        self._messages.append(message)

    def process_messages(self, context: 'GameContext'):
        while self._messages:
            message = self._messages.popleft()
            for component in self._components:
                component.process_message(message, context)
