from typing import Callable

subscribers = {}


def subscribe(event_type: str, fn: Callable):
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data):
    if event_type not in subscribers:
        print(f"Event {event_type} does not exist")
        return
    for fn in subscribers[event_type]:
        fn(data)
