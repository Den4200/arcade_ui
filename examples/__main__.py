import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: python -m examples <login / leaderboard>')
        sys.exit(1)

    if sys.argv[1] == 'login':
        from examples.login import main
        main()

    elif sys.argv[1] == 'leaderboard':
        from examples.leaderboard import main
        main()

    else:
        print('Usage: python -m examples <login / leaderboard>')
        sys.exit(1)


if __name__ == "__main__":
    main()
