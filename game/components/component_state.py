from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .component_type import ComponentType


@dataclass
class ComponentState:
    component_type: 'ComponentType'
