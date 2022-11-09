from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Device:
    name: str
    value1: int
    value2: int

    def __str__(self):
        return f'{self.name} ({self.value1}/{self.value2})'


@dataclass
class CreatureModifier:
    device: Device
    next_modifier: ClassVar = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def set_froze(self):
        if self.next_modifier:
            self.next_modifier.set_froze()


@dataclass
class NoModidier(CreatureModifier):

    def set_froze(self):
        print('Отменить изменения')


@dataclass
class DoubleModifier(CreatureModifier):

    def set_froze(self):
        print(f'Удвоение значения {self.device.name}')
        self.device.value1 *= 2
        self.device.value2 /= 2
        super().set_froze()


if __name__ == '__main__':
    stove = Device('Печь', 100, 100)
    print(stove)

    root = CreatureModifier(stove)

    #root.add_modifier(NoModidier(stove))

    root.add_modifier(DoubleModifier(stove))
    root.add_modifier(DoubleModifier(stove))

    root.set_froze()  # apply modifiers
    print(stove)
