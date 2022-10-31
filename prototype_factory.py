from copy import deepcopy
from dataclasses import dataclass
from typing import ClassVar


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


@dataclass
class Postamp:
    recipient: str
    postamp: str
    address: Address

    def __str__(self):
        return f'Получатель {self.recipient}, Почтамп: {self.postamp} ' +\
               f'{self.address}'


@dataclass
class PostampFactory():
    мoscow: ClassVar = Postamp('', 'Центральный', Address('RU', 'Москва', ''))
    vladivostok: ClassVar = Postamp('', 'Южный', Address('RU', 'Владивосток', ''))

    @staticmethod
    def __new_postman(proto, name):
        result = deepcopy(proto)
        result.recipient = name
        return result

    @staticmethod
    def moscow_postamp(name):
        return PostampFactory.__new_postman(PostampFactory.мoscow, name)

    @staticmethod
    def vladivostok_postamp(name):
        return PostampFactory.__new_postman(PostampFactory.vladivostok, name)


if __name__ == '__main__':
    recipient1 = PostampFactory.moscow_postamp('Иванов Иван')
    recipient2 = PostampFactory.vladivostok_postamp('Петров Петр')

    print(recipient1)
    print(recipient2)
