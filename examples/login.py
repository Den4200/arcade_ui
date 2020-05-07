import arcade
from arcade_gui import TextBox, TextInput


WINDOW_SIZE = (1280, 720)

USERNAME = 'test'
PASSWORD = 'password'


class LoginInput(TextInput):

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_enter(self, text):
        self.ctx.login()


class LoginExample(arcade.Window):

    def __init__(self):
        super().__init__(*WINDOW_SIZE, 'Test Window')

        self.username_input = None
        self.password_input = None

        self.status_text = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.username_input = LoginInput(
            ctx=self,
            center_x=WINDOW_SIZE[0] / 2,
            center_y=WINDOW_SIZE[1] / 2 + 25
        )
        self.password_input = LoginInput(
            ctx=self,
            center_x=WINDOW_SIZE[0] / 2,
            center_y=WINDOW_SIZE[1] / 2 - 25,
            protected=True
        )

    def on_mouse_press(self, x, y, button, modifiers):
        self.username_input.on_mouse_press(x, y, button, modifiers)
        self.password_input.on_mouse_press(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        self.username_input.on_key_press(key, modifiers)
        self.password_input.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.username_input.on_key_release(key, modifiers)
        self.password_input.on_key_release(key, modifiers)

    def on_draw(self):
        arcade.start_render()
        self.username_input.draw()
        self.password_input.draw()

        if self.status_text is not None:
            self.status_text.draw()

    def on_update(self, delta_time=1/60):
        self.username_input.on_update(delta_time)
        self.password_input.on_update(delta_time)

    def login(self):
        if self.username_input.text == USERNAME and self.password_input.text == PASSWORD:
            display_text = 'Login successful.'
        else:
            display_text = 'Incorrect username or password.'

        self.status_text = arcade.draw_text(
            text=display_text,
            start_x=WINDOW_SIZE[0] / 2,
            start_y=WINDOW_SIZE[1] / 2 - 60,
            color=arcade.color.BLACK,
            align='center',
            anchor_x='center',
            anchor_y='center'
        )

        self.status_text = TextBox(
            text=display_text,
            center_x=WINDOW_SIZE[0] / 2,
            center_y=WINDOW_SIZE[1] / 2 - 100,
            width=250,
            height=50
        )
