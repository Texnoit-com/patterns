from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Address:
    country: str
    city: str
    street_address: str

    def __str__(self):
        return f'Пункт отправления {self.street_address},' +\
               f'{self.city}, {self.country}'


@dataclass
class Package:
    sender: str
    address: Address

    def __str__(self):
        return f'Отправитель {self.sender} {self.address}'


if __name__ == '__main__':
    '''Базовая запись'''
    sender = Package("", Address("RU", "Екатеринбург", ""))

    '''Копирование базовой записи'''
    sender1 = deepcopy(sender)
    sender1.sender = "Андрей"
    sender1.address.street_address = "Маяковского 145"
    print(sender1)

    '''Копирование базовой записи'''
    sender2 = deepcopy(sender)
    sender2.sender = "Михаил"
    sender2.address.street_address = "Ленина 45"

    print(sender2)
    print(sender)
