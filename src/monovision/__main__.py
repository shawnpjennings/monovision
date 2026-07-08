"""Entry point: python -m monovision"""

from monovision.core import greet


def main() -> None:
    print(greet("world"))


if __name__ == "__main__":
    main()
