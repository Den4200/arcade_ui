from typing import Any, Callable, List, Tuple, Union

import arcade

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
        node_margin: float = 10,
        scroll_speed: float = 10,
        fill: bool = False,
        fill_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.csscolor.WHITE,
        border: bool = False,
        border_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.BLACK,
        border_width: float = 1
    ) -> None:
        self.center_x = center_x
        self.center_y = center_y

        self.width = width
        self.height = height

        self.nodes = nodes
        self.node_margin = node_margin

        for node in self.nodes:
            node.active = (
                node.center_y - node.height / 2 > self.center_y - self.height / 2 and
                node.center_y + node.height / 2 < self.center_y + self.height / 2
            )

        self.scroll_speed = scroll_speed

        self.fill = fill
        self.fill_color = fill_color

        self.border = border
        self.border_color = border_color
        self.border_width = border_width

        self.mouse_pos = (0, 0)

        if self.fill:
            self.fill_box = arcade.create_rectangle_filled(
                center_x=center_x,
                center_y=center_y,
                width=width,
                height=height,
                color=fill_color
            )

        if self.border:
            self.border_box = arcade.create_rectangle_outline(
                center_x=center_x,
                center_y=center_y,
                width=width,
                height=height,
                color=border_color,
                border_width=border_width
            )

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        self.mouse_pos = (x, y)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        if (
            self.center_x - self.width / 2 < self.mouse_pos[0] < self.center_x + self.width / 2 and
            self.center_y - self.height / 2 < self.mouse_pos[1] < self.center_y + self.height / 2
        ):
            for node in self.nodes:
                node.center_y -= scroll_y * self.scroll_speed
                node.shapes.center_y -= scroll_y * self.scroll_speed
                node.text_sprite.center_y -= scroll_y * self.scroll_speed

                node.active = (
                    node.center_y - node.height / 2 > self.center_y - self.height / 2 and
                    node.center_y + node.height / 2 < self.center_y + self.height / 2
                )

    def add_node(self, node_cls: Any, auto_position: bool = True) -> Callable[[Any], None]:
        def inner(**kwargs: Any) -> None:
            if auto_position:

                if len(self.nodes) > 0:
                    last = self.nodes[-1]

                    node = node_cls(
                        center_x=self.center_x,
                        center_y=last.center_y - last.height / 2 - self.node_margin - kwargs['height'] / 2,
                        **kwargs
                    )
                else:
                    node = node_cls(
                        center_x=self.center_x,
                        center_y=self.center_y + self.height / 2 - self.node_margin - kwargs['height'] / 2,
                        **kwargs
                    )

            else:
                node = node_cls(**kwargs)

            node.active = (
                node.center_y - node.height / 2 > self.center_y - self.height / 2 and
                node.center_y + node.height / 2 < self.center_y + self.height / 2
            )

            self.nodes.append(node)

        return inner

    def draw(self) -> None:
        if self.fill:
            self.fill_box.draw()

        for node in self.nodes:
            if node.active:
                node.draw()

        if self.border:
            self.border_box.draw()
