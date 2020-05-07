import arcade

from examples.login import LoginExample


def main():
    window = LoginExample()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
