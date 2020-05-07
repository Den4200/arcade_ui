import arcade
from arcade_gui import TextBox
from arcade_gui.views import ListView


WINDOW_SIZE = (1280, 720)
SCORES = [
    ('dennis', 34),
    ('joe', 43),
    ('bob', 12),
    ('dennis', 54),
    ('bob', 102),
    ('joe', 324),
    ('bob', 24),
    ('joe', 35),
    ('dennis', 163),
    ('joe', 65)
]


class LeaderboardExample(arcade.Window):

    def __init__(self):
        super().__init__(*WINDOW_SIZE, 'Leaderboard Example')

        self.list_view = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.list_view = ListView(
            center_x=WINDOW_SIZE[0] / 2,
            center_y=WINDOW_SIZE[1] / 2,
            height=WINDOW_SIZE[1]
        )

        for idx, (name, score) in enumerate(sorted(SCORES, key=lambda tup: tup[1])):
            self.list_view.nodes.append(
                TextBox(
                    text=f'{name} - {score}',
                    center_x=WINDOW_SIZE[0] / 2,
                    center_y=WINDOW_SIZE[1] - (len(SCORES) - idx) * 100,
                    width=WINDOW_SIZE[0] / 8 * 7,
                    height=80,
                    border_width=3
                )
            )

    def on_draw(self):
        arcade.start_render()
        self.list_view.draw()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.list_view.on_mouse_scroll(x, y, scroll_x, scroll_y)
