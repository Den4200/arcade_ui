import arcade
from arcade_gui import EventMap, TextBox, View
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


class LeaderboardExample(View):

    def __init__(self, event_map):
        super().__init__(event_map)

        self.list_view = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def on_show(self):
        self.event_map.clear()

        self.list_view = ListView(
            center_x=WINDOW_SIZE[0] / 2,
            center_y=WINDOW_SIZE[1] / 2,
            width=WINDOW_SIZE[0] / 8 * 7,
            height=WINDOW_SIZE[1]
        )

        for idx, (name, score) in enumerate(sorted(SCORES, key=lambda tup: tup[1])):
            self.list_view.add_node(
                TextBox(
                    text=f'{name} - {score}',
                    center_x=WINDOW_SIZE[0] / 2,
                    center_y=WINDOW_SIZE[1] - (len(SCORES) - idx) * 100,
                    width=WINDOW_SIZE[0] / 8 * 7,
                    height=80,
                    border_width=3
                )
            )

        super().setup()

    def on_draw(self):
        arcade.start_render()
        self.list_view.draw()


def main():
    window = arcade.Window(*WINDOW_SIZE, 'Leaderboard Example')
    event_map = EventMap()

    window.show_view(LeaderboardExample(event_map))
    arcade.run()
