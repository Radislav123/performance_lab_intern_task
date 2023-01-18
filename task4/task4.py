import sys


def get_args() -> list:
    args = [x for x in sys.argv[1:]]
    return args


def calculate() -> int:
    with open(get_args()[0], 'r') as file:
        data = list(map(int, file.read().split()))
        data.sort()
        # можно взять любое значение из [data[len(data) // 2], data[len(data) // 2 - 1]]
        median = data[len(data) // 2]
        lengths = [abs(median - x) for x in data]
        result = sum(lengths)
    return result


if __name__ == "__main__":
    print(calculate())
