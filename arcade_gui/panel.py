from typing import List, Tuple, Type, Union

import arcade

from arcade_gui.buttons import ButtonBehavior
from arcade_gui.widgets import InteractiveWidget


class Panel(InteractiveWidget, ButtonBehavior):
    __widget_name__ = 'panel'

    def __init__(
        self,
        center_x: float,
        center_y: float,
        width: float,
        height: float,
        fill_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.WHITE,
        border_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.BLACK,
        border_width: float = 1,
        moveable: bool = True,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.center_x = center_x
        self.center_y = center_y

        self.width = width
        self.height = height

        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width

        self.moveable = moveable

        self.fill_box = arcade.create_rectangle_filled(
            center_x=center_x,
            center_y=center_y,
            width=width,
            height=height,
            color=fill_color
        )
        self.outline_box = arcade.create_rectangle_outline(
            center_x=center_x,
            center_y=center_y,
            width=width,
            height=height,
            color=border_color,
            border_width=border_width
        )

        self.shapes = arcade.ShapeElementList()
        self.shapes.append(self.fill_box)
        self.shapes.append(self.outline_box)

        self.elements: List[Type[InteractiveWidget]] = list()

    def add_element(self, element: Type[InteractiveWidget]) -> None:
        if not isinstance(element, InteractiveWidget):
            raise TypeError(f'Element should be a subclass of InteractiveWidget')

        self.elements.append(element)

    def remove_element(self, element: Type[InteractiveWidget]) -> None:
        self.elements.remove(element)

    def move_center_x(self, delta_x: float) -> None:
        self.shapes.move(delta_x, 0)

        for element in self.elements:
            element.move_center_x(delta_x)

    def move_center_y(self, delta_y: float) -> None:
        self.shapes.move(0, delta_y)

        for element in self.elements:
            element.move_center_y(delta_y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        if self.pressed:
            self.move_center_x(dx)
            self.move_center_y(dy)

    def draw(self) -> None:
        self.shapes.draw()

        for element in self.elements:
            element.draw()
