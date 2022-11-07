from dataclasses import dataclass
from typing import ClassVar


@dataclass
class User:
    name: str

@dataclass
class User2:
    name: str
    strings: ClassVar = []
    names: ClassVar = []

    def __post_init__(self):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
        self.names = [get_or_add(x) for x in self.name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


if __name__ == '__main__':
    u1 = User2('Александр Петров')
    u2 = User2('Владимир Конев')
    u3 = User2('Александр Конев')
    print(u1.names)
    print(u2.names)
    print(u3.names)
    print(User2.strings)