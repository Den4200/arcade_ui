import arcade
from arcade_ui import EventMap, TextButton, TextInput, View
from arcade_ui.views import ListView


WINDOW_SIZE = (1280, 720)


class TaskInput(TextInput):
    __widget_name__ = 'task_input'

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_enter(self, text):
        self.ctx.add_task()


class AddTaskButton(TextButton):
    __widget_name__ = 'add_task_button'

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_submit(self):
        self.ctx.add_task()


class TaskNode(TextButton):
    __widget_name__ = 'task_node'

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_submit(self):
        self.ctx.remove_task(self)


class TodoList(View):

    def __init__(self, event_map):
        super().__init__(event_map)

        self.list_view = None
        self.task_input = None
        self.add_task_button = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def on_show(self):
        self.event_map.clear()

        self.list_view = ListView(
            center_x=WINDOW_SIZE[0] / 4,
            center_y=WINDOW_SIZE[1] / 2,
            width=WINDOW_SIZE[0] / 4,
            height=WINDOW_SIZE[1] / 8 * 7,
            fill=True,
            border=True,
            border_width=5,
            fill_color=(210, 240, 240)
        )

        self.task_input = TaskInput(
            ctx=self,
            center_x=WINDOW_SIZE[0] / 4 * 3,
            center_y=WINDOW_SIZE[1] / 2,
            width=WINDOW_SIZE[0] / 4,
            height=25,
            border_width=3
        )

        self.add_task_button = AddTaskButton(
            ctx=self,
            text='Add Task',
            center_x=WINDOW_SIZE[0] / 4 * 3,
            center_y=WINDOW_SIZE[1] / 2 - 40,
            width=120,
            height=25,
            border_width=3,
            viewport=[0, 0]
        )

        super().setup()

    def on_draw(self):
        arcade.start_render()
        self.list_view.draw()
        self.task_input.draw()
        self.add_task_button.draw()

    def add_task(self):
        if self.task_input.text:
            node = self.list_view.add_node(TaskNode)(
                ctx=self,
                text=self.task_input.text,
                width=WINDOW_SIZE[0] / 4 - 20,
                height=30,
                border_width=3,
                viewport=[0, 0]
            )
            self.event_map.add(node)
            self.task_input.clear_text()

    def remove_task(self, node):
        self.list_view.remove_node(node)
        self.event_map.remove(node)


def main():
    window = arcade.Window(*WINDOW_SIZE, 'Leaderboard Example')
    event_map = EventMap()

    window.show_view(TodoList(event_map))
    arcade.run()


if __name__ == "__main__":
    main()
