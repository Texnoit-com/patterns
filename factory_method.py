from dataclasses import dataclass
from math import cos, sin


@dataclass
class Point:
    x: float
    y: float

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(3, 6)
    print(p1)
    print(p2)
