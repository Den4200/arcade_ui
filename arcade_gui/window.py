from typing import Any

import arcade

from arcade_gui.event_map import EventMap
from arcade_gui.widgets import _widgets


class Window(arcade.Window):

    def __init__(self, event_map: EventMap, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.event_map = event_map

    def setup(self) -> None:
        for name, widgets in _widgets.items():
            for widget in widgets:
                self.event_map.add(widget)

    def on_key_press(self, key: int, modifiers: int) -> None:
        self.event_map.execute('on_key_press', key, modifiers)

    def on_key_release(self, key: int, modifiers: int) -> None:
        self.event_map.execute('on_key_release', key, modifiers)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int) -> None:
        self.event_map.execute('on_mouse_drag', x, y, dx, dy, buttons, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        self.event_map.execute('on_mouse_motion', x, y, dx, dy)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.event_map.execute('on_mouse_press', x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.event_map.execute('on_mouse_release', x, y, button, modifiers)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        self.event_map.execute('on_mouse_scroll', x, y, scroll_x, scroll_y)

    def on_resize(self, width: float, height: float) -> None:
        self.event_map.execute('on_resize', width, height)

    def on_update(self, delta_time: float) -> None:
        self.event_map.execute('on_update', delta_time)
