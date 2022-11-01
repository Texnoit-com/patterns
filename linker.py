from dataclasses import dataclass


@dataclass
class LinkerObject:
    product: str = None

    def __post_init__ (self):
        self.children = []
        self._name  = 'Посылка'

    @property
    def name(self) -> str:
        return self._name

    def _print(self, items, depth) -> None:
        items.append('*' * depth)
        if self.product:
            items.append(self.product)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self) -> str:
        items = []
        self._print(items, 0)
        return ''.join(items)


class Meter(LinkerObject):
    @property
    def name(self):
        return '(метр)'


class Kilogram(LinkerObject):
    @property
    def name(self):
        return '(кг))'


if __name__ == '__main__':
    group1 = LinkerObject()
    group1.children.append(Meter('Ткань'))
    group1.children.append(Kilogram('Пуговицы'))

    group2 = LinkerObject()
    group2.children.append(Meter('Шнурок'))
    group2.children.append(Kilogram('Брошки'))
    group1.children.append(group2)

    print(group1)
