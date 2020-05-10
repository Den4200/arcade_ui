from typing import Any, List

from arcade_gui.widgets import InteractiveWidget


class ListView(InteractiveWidget):
    __widget_name__ = 'list_view'

    def __init__(
        self,
        center_x: float,
        center_y: float,
        width: float,
        height: float,
        nodes: List[Any] = list(),
        scroll_speed: float = 10,
        margin: float = 10
    ) -> None:
        self.center_x = center_x
        self.center_y = center_y

        self.width = width
        self.height = height

        self.nodes = nodes

        self.scroll_speed = scroll_speed
        self.margin = margin

        self.mouse_pos = (0, 0)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        self.mouse_pos = (x, y)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        if (
            self.center_x - self.width / 2 < self.mouse_pos[0] < self.center_x + self.width / 2 and
            self.center_y - self.height / 2 < self.mouse_pos[1] < self.center_y + self.height / 2
        ):
            for node in self.nodes:
                # node.center_y -= scroll_y * self.scroll_speed
                node.shapes.center_y -= scroll_y * self.scroll_speed
                node.text_sprite.center_y -= scroll_y * self.scroll_speed

    def draw(self) -> None:
        for node in self.nodes:
            node.draw()
