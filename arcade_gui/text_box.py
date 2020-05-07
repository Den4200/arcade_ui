from typing import Tuple, Union

import arcade


class TextBox:

    def __init__(
        self,
        text: str,
        center_x: float,
        center_y: float,
        width: float,
        height: float,
        box_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.WHITE,
        border_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.BLACK,
        border_width: float = 1,
        text_color: Union[Tuple[int, int, int], Tuple[int, int, int, int]] = arcade.color.BLACK,
        bold: bool = False,
        italic: bool = False,
        font_name: Union[str, Tuple[str, ...]] = ('calibri', 'arial'),
        font_size: float = 12,
        anchor_x: str = 'center',
        anchor_y: str = 'center',
        horizontal_margin: float = 5,
        vertical_margin: float = 5
    ):
        self._text = text

        self._center_x = center_x
        self._center_y = center_y

        self.width = width
        self.height = height

        self.box_color = box_color
        self.border_color = border_color
        self.border_width = border_width

        self.text_color = text_color
        self.bold = bold
        self.italic = italic
        self.font_name = font_name
        self.font_size = font_size

        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

        self.horizontal_margin = horizontal_margin
        self.vertical_margin = vertical_margin

        self.shapes = arcade.ShapeElementList()
        self.shapes.append(
            arcade.create_rectangle_filled(
                center_x=center_x,
                center_y=center_y,
                width=width,
                height=height,
                color=box_color
            ),
        )
        self.shapes.append(
            arcade.create_rectangle_outline(
                center_x=center_x,
                center_y=center_y,
                width=width,
                height=height,
                color=border_color,
                border_width=border_width
            )
        )

        if anchor_x == 'left':
            self.start_x = center_x - (width / 2) + horizontal_margin
        elif anchor_x == 'center':
            self.start_x = center_x
        elif anchor_x == 'right':
            self.start_x = center_x + (width / 2) - horizontal_margin
        else:
            raise ValueError('ListView.start_x must be "left", "center", or "right"')

        if anchor_y == 'bottom':
            self.start_y = center_y - (height / 2) + vertical_margin
        elif anchor_y == 'center':
            self.start_y = center_y
        elif anchor_y == 'top':
            self.start_y = center_y + (height / 2) - vertical_margin
        else:
            raise ValueError('ListView.start_y must be "bottom", "center", or "top"')

        self.text_sprite = arcade.draw_text(
            text=text,
            start_x=self.start_x,
            start_y=self.start_y,
            color=text_color,
            font_name=font_name,
            font_size=font_size,
            bold=bold,
            italic=italic,
            anchor_x=anchor_x,
            anchor_y=anchor_y
        )

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self.text_sprite = arcade.draw_text(
            text=value,
            start_x=self.start_x,
            start_y=self.start_y,
            color=self.text_color,
            font_name=self.font_name,
            font_size=self.font_size,
            bold=self.bold,
            italic=self.italic,
            anchor_x=self.anchor_x,
            anchor_y=self.anchor_y
        )
        self._text = value

    @property
    def center_x(self) -> float:
        return self._center_x

    @center_x.setter
    def center_x(self, value: float) -> None:
        self.shapes.center_x = value
        self.text_sprite.center_x = value
        self._center_x = value

    @property
    def center_y(self) -> float:
        return self._center_y

    @center_y.setter
    def center_y(self, value: float) -> None:
        self.shapes.center_y = value
        self.text_sprite.center_y = value
        self._center_y = value

    def draw(self) -> None:
        self.shapes.draw()
        self.text_sprite.draw()
