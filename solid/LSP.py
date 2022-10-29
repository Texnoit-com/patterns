from dataclasses import dataclass


@dataclass
class Rectangle:
    _width: int
    _height: int

    @property
    def width(self):
        return self._width

    @width.setter
    def widht(self, value):
        if value <= 0:
            raise Exception
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise Exception
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


@dataclass
class Square(Rectangle):
    def __init__(self, size: int):
        Rectangle.__init__(self, size, size)

    @Rectangle.widht.setter
    def widht(self, value):
        self._widht = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._widht = self._height = value


if __name__ == '__main__':

    print('Прямоугольник')
    rs = Rectangle(5, 10)
    print(rs.area)
    rs.height = 20
    print(rs.area)

    print('Квадрат')
    sq = Square(5)
    print(sq.area)
    sq.height = 10
    print(sq.area)
