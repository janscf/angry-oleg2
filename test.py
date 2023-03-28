from collections import defaultdict
import inspect
from typing import Dict, Type


class AttackEvent:
    pass


def event_handler(event_type: Type):
    def wrapper(outer_func):
        handled_events = getattr(outer_func, '_handled_events', [])
        handled_events.append(event_type)
        setattr(outer_func, '_handled_events', handled_events)
        return outer_func

    return wrapper


class A:
    def __init__(self) -> None:
        self._event_handlers: Dict[Type, list] = self._get_event_handlers()

    def send_event(self, event):
        pass

    @event_handler(AttackEvent)
    def attack_handler(self, event):
        print('Attack')

    def __get_event_handlers(self) -> Dict[Type, list]:
        handlers = defaultdict(list)
        for _, method in inspect.getmembers(self, inspect.ismethod):
            if hasattr(method, '_handled_events'):
                for event_type in getattr(method, '_handled_events'):
                    handlers[event_type].append(method)

        return handlers

a = A()
