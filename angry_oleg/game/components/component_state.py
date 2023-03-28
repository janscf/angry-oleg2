from dataclasses import dataclass


@dataclass(frozen=True)
class ComponentState:
    component_type: str
