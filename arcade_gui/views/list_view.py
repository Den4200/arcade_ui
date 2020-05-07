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
        if self.nodes[0].center_y + self.nodes[0].width / 2 <= self.height - self.margin:
            return

        if self.nodes[-1].center_y - self.nodes[-1].width / 2 <= self.margin:
            return

        for node in self.nodes:
            node.center_y += scroll_y * self.scroll_speed
