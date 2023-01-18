import math
import sys
from typing import List


class Circle:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def check(self, x, y) -> int:
        center_distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        if center_distance == self.radius:
            point_result = 0
        elif center_distance < self.radius:
            point_result = 1
        else:
            point_result = 2
        return point_result


def get_args() -> list:
    args = [x for x in sys.argv[1:]]
    return args


def calculate() -> List[int]:
    circle_filepath, points_filepath = get_args()
    with open(circle_filepath, 'r') as circle_file, open(points_filepath, 'r') as points_file:
        circle = Circle(*map(float, circle_file.readline().split()), float(circle_file.readline()))
        results = []
        for line in points_file:
            point = [x for x in map(float, line.split())]
            results.append(circle.check(*point))
    return results


if __name__ == "__main__":
    for result in calculate():
        print(result)
