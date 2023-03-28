from abc import ABC, abstractmethod
from typing import Any, Optional


class Command(ABC):
    @abstractmethod
    def execute(self, parameter: Optional[Any] = None):
        pass
