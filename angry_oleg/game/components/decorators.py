from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from game.events.event import Event


HANDLED_EVENTS_ATTR = '_handled_events'


def event_handler(event_type: Type['Event']):
    def wrapper(outer_func):
        handled_events = getattr(outer_func, HANDLED_EVENTS_ATTR, [])
        handled_events.append(event_type)
        setattr(outer_func, HANDLED_EVENTS_ATTR, handled_events)
        return outer_func

    return wrapper
