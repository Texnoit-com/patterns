from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class ISite(ABC):

    @abstractmethod
    def get_page(self, page: int) -> str:
        pass


@dataclass
class Site(ISite):
    def get_page(self, page: int) -> str:
        return f'Загрузка страницы {page}'


@dataclass
class SiteProxy:
    __site: ISite
    __cache: ClassVar = {}

    def get_page(self, page: int) -> str:
        text: str = ''
        if self.__cache.get(page) is not None:
            text = self.__cache[page]
            return text + 'из кеша'
        text = self.__site.get_page(page)
        self.__cache[page] = text
        return text


if __name__ == '__main__':
    site1: ISite = SiteProxy(Site())

    print(site1.get_page(1))
    print(site1.get_page(2))
    print(site1.get_page(2))
    print(site1.get_page(1))
