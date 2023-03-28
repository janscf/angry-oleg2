from dataclasses import dataclass
from typing import Iterable
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from game.components import ComponentState


@dataclass(frozen=True)
class ObjectState:
    object_id: UUID
    tag: str
    components: Iterable['ComponentState']
