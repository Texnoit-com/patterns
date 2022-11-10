from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar


@dataclass
class BankAccount:
    balance: int = 0
    OVERDRAFT_LIMIT: ClassVar = -10000

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f'Сумма снятия {amount}, баланс = {self.balance}')

    def withdraw(self, amount: int) -> bool:
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Платеж проведен {amount}, баланс = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Баланс = {self.balance}'


class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass
    @abstractmethod
    def undo(self):
        pass


@dataclass
class BankAccountCommand(Command):
    account: BankAccount
    action: int
    amount: int
    success: ClassVar = None

    class Action(Enum):
        DEPOSIT  = 0
        WITHDRAW = 1

    def invoke(self) -> None:
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self) -> None:
        # для простоты сделаем возврат из функции
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    Ivan = BankAccount()
    cmd = BankAccountCommand(Ivan, BankAccountCommand.Action.DEPOSIT, 10000)
    cmd.invoke()
    print('Изначальный депозит 10000:', Ivan)

    cmd.undo()
    print('Отмена депозита:', Ivan)


