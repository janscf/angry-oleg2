from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .component_type import ComponentType


@dataclass(frozen=True)
class ComponentState:
    component_type: 'ComponentType'
