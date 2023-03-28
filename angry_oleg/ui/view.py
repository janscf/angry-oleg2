from abc import ABC, abstractmethod
from typing import Optional

from game import GameState


class View(ABC):
    def __init__(self, parent: Optional['View'] = None):
        self._parent = parent

    @abstractmethod
    def render_state(self, state: 'GameState'):
        pass
