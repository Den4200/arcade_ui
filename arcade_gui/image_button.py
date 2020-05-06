from typing import Any, List

import arcade

from arcade_gui.utils import check_point_for_collision


class ImageButton(arcade.Sprite):

    def __init__(
        self,
        clicked: str,
        normal: str,
        viewport: List[float, float],  # Must be a mutable object!
        **kwargs: Any
    ) -> None:
        super().__init__(filename=normal, **kwargs)

        self.clicked = arcade.load_texture(clicked)
        self.normal = arcade.load_texture(normal)

        self.viewport = viewport

        self.pressed = False

    def on_mouse_press(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            if check_point_for_collision(
                (x, y),
                self.center_x - self.viewport[0] - self.width / 2,
                self.center_x - self.viewport[0] + self.width / 2,
                self.center_y - self.viewport[1] - self.width / 2,
                self.center_y - self.viewport[1] + self.width / 2
            ):
                self.texture = self.clicked
                self.pressed = True

    def on_mouse_release(self, x, y, button, modifiers) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            if check_point_for_collision(
                (x, y),
                self.center_x - self.viewport[0] - self.width / 2,
                self.center_x - self.viewport[0] + self.width / 2,
                self.center_y - self.viewport[1] - self.width / 2,
                self.center_y - self.viewport[1] + self.width / 2
            ):
                self.on_submit()
                self.texture = self.normal
                self.pressed = False

    def on_submit(self) -> None:
        pass
