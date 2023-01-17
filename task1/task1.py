import sys
from typing import Iterable


def get_args() -> Iterable:
    args = [int(x) for x in sys.argv[1:]]
    return args


def find_path() -> str:
    n, m = get_args()
    current = 1
    path = []
    found = False
    while not found:
        path.append(current)
        current = (current + m - 1) % n
        found = (current - 1) % n == 0
    path = [n if x == 0 else x for x in path]
    return "".join(map(str, path))


if __name__ == "__main__":
    print(find_path())
