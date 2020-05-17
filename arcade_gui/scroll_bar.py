from enum import Enum
from typing import Tuple, Union
from dataclasses import dataclass

import arcade


class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Position(Enum):
    END = -1
    START = 0


@dataclass
class RectangleBounds:
    x_left: int
    y_bottom: int
    width: int
    height: int

    def get_bounds(self) -> Tuple[int, int, int, int]:
        return self.x_left, self.y_bottom, self.width, self.height

    def get_center_bounds(self) -> Tuple[int, int, int, int]:
        return self.center_x, self.center_y, self.width, self.height

    @property
    def bottom_left_corner(self) -> Tuple[int, int]:
        return self.x_left, self.y_bottom

    @property
    def bottom_right_corner(self) -> Tuple[int, int]:
        return self.x_left + self.width, self.y_bottom

    @property
    def top_right_corner(self) -> Tuple[int, int]:
        return self.x_left + self.width, self.y_bottom + self.height

    @property
    def top_left_corner(self) -> Tuple[int, int]:
        return self.x_left, self.y_bottom + self.height

    @property
    def center_x(self) -> int:
        return self.x_left + int(round(self.width / 2))

    @property
    def center_y(self) -> int:
        return self.y_bottom + int(round(self.height / 2))

    @property
    def top_y(self) -> int:
        return self.y_bottom + self.height

    @property
    def right_x(self) -> int:
        return self.x_left + self.width


@dataclass
class ScrollBarAdjustmentEvents:
    """
    track is sent out when the user drags the scroll bar's thumb.
    unit_increment is sent out when the user clicks in the left arrow of a horizontal scroll bar,
        or the top arrow of a vertical scroll bar, or makes the equivalent gesture from the keyboard.
    unit_decrement is sent out when the user clicks in the right arrow of a horizontal scroll bar,
        or the bottom arrow of a vertical scroll bar, or makes the equivalent gesture from the keyboard.
    block_increment is sent out when the user clicks in the track, to the left of the thumb on a horizontal
        scroll bar, or above the thumb on a vertical scroll bar. By convention, the Page Up key is equivalent,
        if the user is using a keyboard that defines a Page Up key.
    block_decrement is sent out when the user clicks in the track, to the right of the thumb on a horizontal
        scroll bar, or below the thumb on a vertical scroll bar. By convention, the Page Down key is equivalent,
        if the user is using a keyboard that defines a Page Down key.
    """
    track: Tuple[None, callable]
    unit_increment: Tuple[None, callable]
    unit_decrement: Tuple[None, callable]
    block_increment: Tuple[None, callable]
    block_decrement: Tuple[None, callable]


class ScrollThumb:
    def __init__(self, width: int, height: int, center_x: int, center_y: int):
        self.width = width
        self.height = height

        self.center_x = center_x
        self.center_y = center_y

    def is_being_hovered(self, mouse_x: float, mouse_y: float) -> bool:
        half_width = self.width // 2
        half_height = self.height // 2

        return (
            self.center_x - half_width < mouse_x < self.center_x + half_width and
            self.center_y - half_height < mouse_y < self.center_y + half_height
        )

    def move(self, center_x: int, center_y: int) -> None:
        """To be overwritten by your implementation"""
        pass

    def draw(self):
        """To be overwritten by your implementation"""
        pass


class ScrollThumbSprite(ScrollThumb):
    def __init__(self, width: int, height: int, center_x: int = 0, center_y: int = 0):
        super().__init__(width, height, center_x, center_y)

        self._thumb = None
        self._create_thumb(self.center_x, self.center_y)

    def _create_thumb(self, center_x: int, center_y: int) -> None:
        self.center_x = center_x
        self.center_y = center_y

        self._thumb = arcade.create_rectangle_filled(
            self.center_x,
            self.center_y,
            self.width,
            self.height,
            arcade.color.RED,
        )

    def move(self, center_x: int, center_y: int) -> None:
        self._create_thumb(center_x, center_y)

    def draw(self):
        self._thumb.draw()


class ScrollTrack:
    def __init__(self, bounds: RectangleBounds, border_width: int, orientation: Orientation):
        self._bounds = bounds
        self._border_width = border_width
        self._orientation = orientation
        self._track = self._create_track_outline()

    def _create_track_outline(self) -> arcade.Shape:
        return arcade.create_rectangle_outline(
            *self._bounds.get_center_bounds(),
            arcade.color.BRITISH_RACING_GREEN,
            self._border_width
        )

    @property
    def bounds(self) -> RectangleBounds:
        return self._bounds

    @property
    def border_width(self):
        return self._border_width

    @property
    def center_x(self) -> int:
        return self._bounds.center_x

    @property
    def center_y(self) -> int:
        return self._bounds.center_y

    @property
    def size(self) -> int:
        """
        Returns a int that is, based on orientation:
          vertical - represents height.
          horizontal - represents width
        """
        if self._orientation == Orientation.VERTICAL:
            return self._bounds.height

        elif self._orientation == Orientation.HORIZONTAL:
            return self._bounds.width

    @property
    def breadth(self) -> int:
        """
        Returns a int that is, based on orientation:
          vertical - represents width.
          horizontal - represents height
        """
        if self._orientation == Orientation.VERTICAL:
            return self._bounds.width

        elif self._orientation == Orientation.HORIZONTAL:
            return self._bounds.height

    @property
    def start_coordinate(self) -> int:
        """
        Returns a int representing:
            If position is vertical:
                coordinate representing bottommost position.
            If position is horizontal:
                coordinate representing the leftmost position.
        """
        if self._orientation == Orientation.VERTICAL:
            return self._bounds.y_bottom
        elif self._orientation == Orientation.HORIZONTAL:
            return self._bounds.x_left

    @property
    def end_coordinate(self) -> int:
        """
        Returns a int representing:
            If position is vertical:
                coordinate representing bottommost position.
            If position is horizontal:
                coordinate representing the rightmost position.
        """
        if self._orientation == Orientation.VERTICAL:
            return self._bounds.y_bottom
        elif self._orientation == Orientation.HORIZONTAL:
            return self._bounds.right_x

    def is_being_hovered(self, mouse_x: float, mouse_y: float) -> bool:
        half_width = self._bounds.width // 2
        half_height = self._bounds.height // 2

        return (
                self._bounds.center_x - half_width < mouse_x < self._bounds.center_x + half_width and
                self._bounds.center_y - half_height < mouse_y < self._bounds.center_y + half_height
        )

    def draw(self):
        self._track.draw()


class ScrollBar:
    def __init__(
        self,
        item_count: int,
        orientation: Orientation,
        track_bounds: RectangleBounds,
        scroll_thumb_start_position: Union[int, Position] = Position.START,
        border_width: int = 1,
    ):
        """
        :param item_count: int total number of items the scrollbar can scroll trough.
        :param orientation: Orientation either vertical or horizontal
        :param track_bounds: RectangleBounds bounds for the track
        :param scroll_thumb_start_position:
            (thumb represents the draggable element).
            You can pass integer representing custom start position
            (has to be in range 0 <= position <= item_count ) or constants:

            Position.START means at top if orientation is vertical
                           and at leftmost if orientation is horizontal
            Position.END   means at bottom if orientation is vertical
                           and at rightmost if orientation is horizontal
        :param border_width: int width of track border
        """
        self._item_count = item_count
        self._orientation = orientation
        self._track = ScrollTrack(track_bounds, border_width, orientation)
        self._thumb_position = self._set_initial_thumb_position(scroll_thumb_start_position)

        self._thumb = ScrollThumbSprite(*self._construct_thumb_size())
        self._thumb.move(*self._construct_thumb_position())

        self._thumb_being_clicked_on = False
        self._thumb_is_being_dragged = False

    def _set_initial_thumb_position(self, thumb_start_position: Union[int, Position]) -> int:
        if isinstance(thumb_start_position, int):
            if thumb_start_position < 0:
                raise ValueError("Initial thumb start position has to be greater than 0.")
            elif thumb_start_position > self._item_count:
                raise ValueError("Initial thumb position cannot exceed item count.")
            else:
                return thumb_start_position - 1

        elif isinstance(thumb_start_position, Position):
            if thumb_start_position == Position.START:
                return 0
            elif thumb_start_position == Position.END:
                return self._item_count - 1

    def _construct_thumb_size(self) -> Tuple[int, int]:
        """
        Returns 2 ints representing thumb width and height.
        """
        if self._orientation == Orientation.VERTICAL:
            width = self._track.breadth - self._track.border_width
            height = int(round(self._track.size / self._item_count))

            return width, height

        elif self._orientation == Orientation.HORIZONTAL:
            width = int(round(self._track.size / self._item_count))
            height = self._track.breadth - self._track.border_width

            return width, height

    def _construct_thumb_position(self) -> Tuple[int, int]:
        """
        Returns 2 ints representing thumb center_x and center_y
        """
        if self._orientation == Orientation.VERTICAL:
            center_x = self._track.center_x
            center_y = self._thumb_position_to_coordinate(self._thumb_position)

            return self._align_thumb(center_x, center_y)

        elif self._orientation == Orientation.HORIZONTAL:
            center_x = self._thumb_position_to_coordinate(self._thumb_position)
            center_y = self._track.center_y

            return self._align_thumb(center_x, center_y)

    def _align_thumb(self, center_x: int, center_y: int) -> Tuple[int, int]:
        if self._orientation == Orientation.VERTICAL:
            center_y += self._thumb.height // 2
        elif self._orientation == Orientation.HORIZONTAL:
            center_x += self._thumb.width // 2

        return center_x, center_y

    def _thumb_position_to_coordinate(self, position: int) -> int:
        per_position = self._track.size // self._item_count
        return self._track.start_coordinate + per_position * position

    @property
    def bounds(self):
        return self._track.bounds

    def increment_thumb(self, count: int = 1):
        if self._thumb_position < self._item_count - 1:
            self._thumb_position += count

            # If we pass the limit reset it
            if self._thumb_position > self._item_count - 1:
                self._thumb_position = self._item_count - 1

            self._thumb.move(*self._construct_thumb_position())

    def decrement_thumb(self, count: int = 1):
        if self._thumb_position > 0:
            self._thumb_position -= count

            # If we pass the limit reset it
            if self._thumb_position < 0:
                self._thumb_position = 0

            self._thumb.move(*self._construct_thumb_position())

    def block_increment(self):
        self.increment_thumb(5)

    def block_decrement(self):
        self.decrement_thumb(5)

    def on_key_press(self, symbol: int, _modifiers: int):
        if symbol == arcade.key.PAGEUP:
            self.block_increment()
        elif symbol == arcade.key.PAGEDOWN:
            self.block_decrement()

    def on_mouse_scroll(self, _x: int, _y: int, _scroll_x: int, scroll_y: int):
        if scroll_y > 0:
            self.increment_thumb()
        elif scroll_y < 0:
            self.decrement_thumb()

    def on_mouse_hover_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if self._track.is_being_hovered(x, y):
            self.on_mouse_scroll(x, y, scroll_x, scroll_y)

    def on_mouse_press(self, x, y, button, _modifiers):
        if self._thumb.is_being_hovered(x, y) and button == arcade.MOUSE_BUTTON_LEFT:
            self._thumb_being_clicked_on = True

    def on_mouse_release(self, _x: float, _y: float, button: int, _modifiers: int):
        if self._thumb_being_clicked_on and button == arcade.MOUSE_BUTTON_LEFT:
            self._thumb_being_clicked_on = False
            self._thumb_is_being_dragged = False

    def on_mouse_motion(self, x: float, y: float, _dx: float, _dy: float):
        if self._thumb_being_clicked_on:
            self._thumb_is_being_dragged = True

        if self._thumb_is_being_dragged:
            self._drag_thumb_snapped(x, y)

    def _drag_thumb_snapped(self, mouse_x: float, mouse_y: float):
        previous_position = self._thumb_position_to_coordinate(self._thumb_position - 1)
        next_position = self._thumb_position_to_coordinate(self._thumb_position + 1)

        if self._orientation == Orientation.VERTICAL:
            if mouse_y < previous_position and self._thumb_position > 0:
                self._thumb_position -= 1
            elif mouse_y > next_position and self._thumb_position < self._item_count - 1:
                self._thumb_position += 1

        elif self._orientation == Orientation.HORIZONTAL:
            if mouse_x < previous_position and self._thumb_position > 0:
                self._thumb_position -= 1
            elif mouse_x > next_position and self._thumb_position < self._item_count - 1:
                self._thumb_position += 1

        self._thumb.move(*self._construct_thumb_position())

    def draw(self):
        self._track.draw()
        self._thumb.draw()
