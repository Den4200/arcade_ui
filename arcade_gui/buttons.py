from typing import Any, List, Tuple, Union

import arcade

from arcade_gui.text_box import TextBox
from arcade_gui.utils import check_point_for_collision
from arcade_gui.widgets import InteractiveWidget


class ButtonBehavior:

    def __init__(
        self,
        viewport: List[float],  # Must be a mutable object!
    ):
        self.viewport = viewport

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> bool:
        if button == arcade.MOUSE_BUTTON_LEFT:
            if check_point_for_collision(
                (x, y),
                self.center_x - self.viewport[0] - self.width / 2,
                self.center_x - self.viewport[0] + self.width / 2,
                self.center_y - self.viewport[1] - self.height / 2,
                self.center_y - self.viewport[1] + self.height / 2
            ):
                self.pressed = True
                return True

            return False

        return False

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> bool:
        if button == arcade.MOUSE_BUTTON_LEFT:
            if check_point_for_collision(
                (x, y),
                self.center_x - self.viewport[0] - self.width / 2,
                self.center_x - self.viewport[0] + self.width / 2,
                self.center_y - self.viewport[1] - self.height / 2,
                self.center_y - self.viewport[1] + self.height / 2
            ):
                self.on_submit()
                self.pressed = False
                return True

            return False

        return False

    def on_submit(self) -> None:
        pass


class ImageButton(InteractiveWidget, ButtonBehavior, arcade.Sprite):
    __widget_name__ = 'image_button'

    def __init__(
        self,
        clicked: str,
        normal: str,
        **kwargs: Any
    ) -> None:
        super().__init__(filename=normal, **kwargs)

        self.clicked = arcade.load_texture(clicked)
        self.normal = arcade.load_texture(normal)

        self.pressed = False

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        if super().on_mouse_press(x, y, button, modifiers):
            self.texture = self.clicked

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:
        if super().on_mouse_release(x, y, button, modifiers):
            self.texture = self.normal


class TextButton(TextBox, ButtonBehavior):
    __widget_name__ = 'text_button'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.secondary_color = tuple(
            value * 0.75 if idx != 3 else value for idx, value in enumerate(self.fill_color)
        )

    def _set_fill_color(self, color: Union[Tuple[int, int, int], Tuple[int, int, int, int]]) -> None:
        self.shapes.remove(self.fill_box)

        self.fill_box = arcade.create_rectangle_filled(
            center_x=self._orig_cx,
            center_y=self._orig_cy,
            width=self.width,
            height=self.height,
            color=color
        )

        # Keep the outline on top
        self.shapes.remove(self.outline_box)
        self.shapes.append(self.fill_box)
        self.shapes.append(self.outline_box)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        if super().on_mouse_press(x, y, button, modifiers):
            self._set_fill_color(self.secondary_color)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:
        if super().on_mouse_release(x, y, button, modifiers):
            self._set_fill_color(self.fill_color)
