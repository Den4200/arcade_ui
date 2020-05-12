from dataclasses import dataclass, field
import inspect
from typing import Callable, List

from arcade_gui.widgets import _widgets


@dataclass
class EventMap:
    on_key_press: List[Callable] = field(default_factory=list)
    on_key_release: List[Callable] = field(default_factory=list)

    on_mouse_drag: List[Callable] = field(default_factory=list)
    on_mouse_motion: List[Callable] = field(default_factory=list)
    on_mouse_press: List[Callable] = field(default_factory=list)
    on_mouse_release: List[Callable] = field(default_factory=list)
    on_mouse_scroll: List[Callable] = field(default_factory=list)

    on_resize: List[Callable] = field(default_factory=list)

    on_update: List[Callable] = field(default_factory=list)

    def add(self, instance) -> None:
        inst_attrs = inspect.getmembers(instance, predicate=inspect.ismethod)

        for inst_attr, method in inst_attrs:
            if inst_attr in self.__dict__:
                self.__dict__[inst_attr].append(method)

    def remove(self, instance) -> None:
        inst_attrs = inspect.getmembers(instance, predicate=inspect.ismethod)

        for inst_attr, method in inst_attrs:
            for attr, methods in self.__dict__.items():
                if method in methods:
                    self.__dict__[attr].remove(method)

    def execute(self, event, *args, **kwargs) -> None:
        events = getattr(self, event, default=None)

        if events is None:
            raise ValueError(f'Event {event} does not exist.')

        for event in events:
            if event(*args, **kwargs) == StopIteration:
                break

    def clear(self) -> None:
        for attr in self.__dict__:
            if attr.startswith('on_'):
                self.__dict__[attr] = list()

        for widget_name in _widgets:
            _widgets[widget_name].clear()
