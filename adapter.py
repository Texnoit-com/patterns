from abc import ABC, abstractmethod
from dataclasses import dataclass


class Scale(ABC):

    @abstractmethod
    def get_weight(self) -> float:
        pass


@dataclass
class RussianScale(Scale):
    __carent_weight: float

    def get_weight(self) -> float:
        return self.__carent_weight


@dataclass
class BritishScale(Scale):
    __carent_weight: float

    def get_weight(self) -> float:
        return self.__carent_weight


@dataclass
class AdapterScale(Scale):
    obj: BritishScale

    def get_weight(self) -> float:
        return self.obj.get_weight() * 0.453


def get_weight_kg(value: float) -> None:
    print(f'Вес в килограммах {value}')


if __name__ == '__main__':
    weight_kg: float = 100.0
    weight_lb: float = 100.0

    value1 = RussianScale(weight_kg)
    value2 = AdapterScale(BritishScale(weight_lb))

    get_weight_kg(value1.get_weight())
    get_weight_kg(value2.get_weight())
