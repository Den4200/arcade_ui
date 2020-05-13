from typing import Tuple, Type, Union

import arcade

from arcade_gui.widgets import InteractiveWidget


class Panel(InteractiveWidget):
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
        moveable: bool = True
    ):
        self.center_x = center_x
        self.center_y = center_y

        self.width = width
        self.height = height

        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width

        self.moveable = moveable

        self.elements = list()

    def add_element(self, element: Type[InteractiveWidget]) -> None:
        if not isinstance(element, InteractiveWidget):
            raise TypeError(f'Element should be a subclass of InteractiveWidget')

        self.elements.append(element)

    def remove_element(self, element: Type[InteractiveWidget]) -> None:
        self.elements.remove(element)
