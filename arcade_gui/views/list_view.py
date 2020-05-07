from typing import Any, List


class ListView:

    def __init__(
        self,
        center_x: float,
        center_y: float,
        height: float,
        nodes: List[Any] = list(),
        scroll_speed: float = 10,
        margin: float = 10
    ) -> None:
        self.center_x = center_x
        self.center_y = center_y

        self.height = height

        self.nodes = nodes

        self.scroll_speed = scroll_speed
        self.margin = margin

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        for node in self.nodes:
            # node.center_y -= scroll_y * self.scroll_speed
            node.shapes.center_y -= scroll_y * self.scroll_speed
            node.text_sprite.center_y -= scroll_y * self.scroll_speed

    def draw(self) -> None:
        for node in self.nodes:
            node.draw()
