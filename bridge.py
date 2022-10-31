from abc import ABC, abstractmethod
from dataclasses import dataclass


class Render(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass


@dataclass
class VectorRender(Render):

    def render_circle(self, radius):
        print(f'Круг радиусом {radius}')


@dataclass
class RasterRender(Render):

    def render_circle(self, radius):
        print(f'Пиклельная картинка круга {radius}')


@dataclass
class Shape():
    render: Render

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass


@dataclass
class Circle(Shape):
    render: Render
    radius: float

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRender()
    vector = VectorRender()
    circle1 = Circle(raster, 5)
    circle2 = Circle(vector, 10)

    circle1.draw()
    circle2.draw()
