from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


@dataclass
class MultiPrinter(Printer):

    def print(self, document):
        '''Реализация печати'''
        pass

    def scan(self, document):
        '''Реализация сканирования'''
        pass


@dataclass
class OldPrinter(Printer):

    def print(self, document):
        '''Реализация печати'''
        pass

    def scan(self, document):
        '''Отсутствия функции сканирования'''
        raise NotImplementedError('Принтер не умеет сканировать,'
                                  'но функцию необходимо описать')
