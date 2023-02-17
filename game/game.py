from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import TYPE_CHECKING, Optional, Dict, List
from uuid import UUID

from game.events.time_passed_event import TimePassedEvent
from .context import GameContext

if TYPE_CHECKING:
    from game.objects import ObjectState
    from game.players.player_spawner import Player, PlayerSpawner
    from game.scenes import Scene


class GameStatus(Enum):
    New = auto()
    Running = auto()
    Finished = auto()


@dataclass(frozen=True)
class GameParameters:
    map_name: Optional[str] = None


@dataclass(frozen=True)
class GameState:
    objects: Dict[UUID, 'ObjectState']


class Game:
    def __init__(self, player_spawner: Optional['PlayerSpawner'] = None):
        self._started_at: Optional[datetime] = None
        self._finished_at: Optional[datetime] = None
        self._scene: Optional['Scene'] = None
        self._players: List['Player'] = []
        self._player_spawner = player_spawner

    @property
    def status(self) -> GameStatus:
        if self._finished_at is not None:
            return GameStatus.Finished

        if self._started_at is not None:
            return GameStatus.Running

        return GameStatus.New

    def load_scene(self, scene: 'Scene'):
        self._scene = scene

    def start(self):
        self._started_at = datetime.now()
        self._finished_at = None

    def end(self):
        self._finished_at = datetime.now()

    def get_state(self) -> GameState:
        return GameState(
            objects={
                game_object.id: game_object.get_state() for game_object in self._scene.get_all_objects()
            }
        )

    def add_player(self) -> UUID:
        player = self._player_spawner.instantiate(self._scene)
        self._players.append(player)
        return player.player_id

    def update(self):
        context = GameContext(scene=self._scene)
        for game_object in self._scene.get_all_objects():
            game_object.raise_event(TimePassedEvent())
            game_object.process_events(context)
