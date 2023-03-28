from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import TYPE_CHECKING, Optional, Dict
from uuid import UUID, uuid4

from game.events.time_passed_event import TimePassedEvent
from game.players import Player


if TYPE_CHECKING:
    from game.objects import ObjectState, Spawner
    from game.scenes import Scene
    from game.scenes.context import ContextProvider


class GameStatus(Enum):
    New = auto()
    Running = auto()
    Finished = auto()


@dataclass(frozen=True)
class GameParameters:
    map_name: Optional[str] = None


@dataclass(frozen=True)
class GameState:
    player: 'Player'
    objects: Dict[UUID, 'ObjectState']


class Game:
    def __init__(
        self,
        context_provider: ContextProvider,
        player_spawner: Optional['Spawner'] = None,
    ):
        self._started_at: Optional[datetime] = None
        self._finished_at: Optional[datetime] = None
        self._scene: Optional['Scene'] = None
        self._player_spawner = player_spawner
        self._players: Dict[UUID, Player] = {}
        self._context_provider = context_provider

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

    def get_state(self, player_id: UUID) -> GameState:
        return GameState(
            player=self._players[player_id],
            objects={game_object.id: game_object.get_state() for game_object in self._scene.get_all_objects()},
        )

    def add_player(self) -> UUID:
        player_object = self._player_spawner.spawn(self._scene)
        player_id = uuid4()
        self._players[player_id] = Player(player_id=player_id, object_id=player_object.id)
        return player_id

    def update(self):
        context = self._context_provider.get_context(scene=self._scene)
        for game_object in self._scene.get_all_objects():
            game_object.send_event(TimePassedEvent())
            game_object.process_events(context)
