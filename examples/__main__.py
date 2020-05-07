import sys

import arcade


def main():
    if len(sys.argv) < 2:
        print('Usage: python -m examples <login / leaderboard>')
        sys.exit(1)

    if sys.argv[1] == 'login':
        from examples.login import LoginExample
        window = LoginExample()

    elif sys.argv[1] == 'leaderboard':
        from examples.leaderboard import LeaderboardExample
        window = LeaderboardExample()

    else:
        print('Usage: python -m examples <login / leaderboard>')
        sys.exit(1)

    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
