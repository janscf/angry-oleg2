from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import TYPE_CHECKING, Optional

from game.messages.time_passed import TimePassedMessage
from .context import GameContext

if TYPE_CHECKING:
    from game.scene import Scene


class GameStatus(Enum):
    NEW = auto()
    RUNNING = auto()
    FINISHED = auto()


@dataclass(frozen=True)
class GameParameters:
    map_name: Optional[str] = None


class Game:
    def __init__(self):
        self.__started_at: Optional[datetime] = None
        self.__finished_at: Optional[datetime] = None
        self.__scene: 'Scene' = None

    @property
    def status(self) -> GameStatus:
        if self.__finished_at is not None:
            return GameStatus.FINISHED

        if self.__started_at is not None:
            return GameStatus.RUNNING

        return GameStatus.NEW

    def load_scene(self, scene: 'Scene'):
        self.__scene = scene

    def start(self):
        self.__started_at = datetime.now()
        self.__finished_at = None

    def end(self):
        self.__finished_at = datetime.now()

    def update(self):
        context = GameContext(scene=self.__scene)
        for game_object in self.__scene.get_all_objects():
            game_object.send_message(TimePassedMessage())
            game_object.process_messages(context)
