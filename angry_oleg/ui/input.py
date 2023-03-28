from typing import Any, Optional

from action_type import ActionType


class Input:
    action: Optional[ActionType] = None

    @classmethod
    def wait_for_user_input(cls):
        key_binding = {
            'w': ActionType.MoveNorth,
            'd': ActionType.MoveEast,
            's': ActionType.MoveSouth,
            'a': ActionType.MoveWest,
        }

        while True:
            key = input('Ваши действия: ').strip()
            if key not in key_binding:
                continue

            cls.action = key_binding[key]
            break
