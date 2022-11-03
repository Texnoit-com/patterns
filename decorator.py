from abc import ABC
from dataclasses import dataclass


class Tag(ABC):
    def __str__(self):
        return ''


@dataclass
class H1(Tag):
    size: int = 14

    def __str__(self):
        return f'Заголовок размером {self.size}'


@dataclass
class Link(Tag):
    site: str = 'http'

    def __str__(self):
        return f'Ссылка на сайт {self.site}'


@dataclass
class Color(Tag):
    tag: Tag
    color: str

    def __str__(self):
        return f'{self.tag} цветом {self.color}'


@dataclass
class Stile(Tag):
    tag: Tag
    inscription: str = 'Normal'

    def __str__(self):
        return f'{self.tag} начертание *{self.inscription}*'


if __name__ == '__main__':
    title = H1()
    print(title)

    red_h1 = Color(title, 'red')
    print(red_h1)

    red_half_transparent_square = Stile(red_h1, 'Курсив')
    print(red_half_transparent_square)
