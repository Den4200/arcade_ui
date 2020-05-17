import arcade
from arcade_gui.scroll_bar import ScrollBar, Position, RectangleBounds, Orientation


WINDOW_SIZE = (1280, 720)


class ScrollBarExample(arcade.Window):

    def __init__(self):
        super().__init__(*WINDOW_SIZE, 'Test Window')

        self.scroll_bar_vertical = None
        self.scroll_bar_horizontal = None

    def setup(self):
        self.scroll_bar_vertical = ScrollBar(
            10,
            Orientation.VERTICAL,
            RectangleBounds(50, 50, 80, 400),
            Position.START
        )

        self.scroll_bar_horizontal = ScrollBar(
            10,
            Orientation.HORIZONTAL,
            RectangleBounds(250, 50, 400, 80),
            Position.START
        )

    def on_mouse_press(self, x, y, button, modifiers):
        self.scroll_bar_vertical.on_mouse_press(x, y, button, modifiers)
        self.scroll_bar_horizontal.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.scroll_bar_vertical.on_mouse_release(x, y, button, modifiers)
        self.scroll_bar_horizontal.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.scroll_bar_vertical.on_mouse_motion(x, y, dx, dy)
        self.scroll_bar_horizontal.on_mouse_motion(x, y, dx, dy)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        # Interact with it no matter where the mouse is at
        self.scroll_bar_vertical.on_mouse_scroll(x, y, scroll_x, scroll_y)
        # Interact with it only if the mouse is currently hovering over it
        self.scroll_bar_horizontal.on_mouse_hover_scroll(x, y, scroll_x, scroll_y)

    def on_key_press(self, symbol: int, modifiers: int):
        self.scroll_bar_vertical.on_key_press(symbol, modifiers)
        self.scroll_bar_horizontal.on_key_press(symbol, modifiers)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.scroll_bar_vertical.draw()
        self.scroll_bar_horizontal.draw()
