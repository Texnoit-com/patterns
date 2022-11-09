from dataclasses import dataclass
from typing import ClassVar


@dataclass
class User:
    name: str
    age: int


@dataclass
class Bank:
    client: User

    def payment(self) -> None:
        print(f'Предоставлен доступ для платежа {self.client.name}')


@dataclass
class BankProxy:
    user: User
    client: ClassVar

    def __post_init__(self):
        self.client = Bank(self.user)

    def payment(self) -> None:
        if self.user.age >= 18:
            self.client.payment()
        else:
            print('Доступ ограничен')


if __name__ == '__main__':
    client1 = BankProxy(User('Иван', 20))
    client1.payment()

    client2 = BankProxy(User('Матвей', 17))
    client2.payment()
