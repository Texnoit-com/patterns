from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


@dataclass
class Product:
    name: str
    color: Color
    size: Size


@dataclass
class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass


class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        pass


@dataclass
class ColorSpecification(Specification):
    color: Color

    def is_satisfied(self, item) -> bool:
        return item.color == self.color


@dataclass
class SizeSpecification(Specification):
    size: Size

    def is_satisfied(self, item) -> bool:
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


@dataclass
class СombinatorSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    tomat = Product('Tomat', Color.RED, Size.SMALL)

    products = [apple, tree, tomat]

    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'- {p.name} is green')

    print('Проверка нескольких параметров фильтра - комбинатор')
    small_green = СombinatorSpecification(SizeSpecification(Size.SMALL),
                                          ColorSpecification(Color.GREEN))
    for p in bf.filter(products, small_green):
        print(f'- {p.name} is small and green')
