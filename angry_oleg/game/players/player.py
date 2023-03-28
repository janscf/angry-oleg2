from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class Player:
    player_id: UUID
    object_id: UUID
    phase: str = ''
