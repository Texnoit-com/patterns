from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    NEIGHBOR = 2


@dataclass
class Folder:
    name: str


@dataclass
class RelationshipBrowser(ABC):

    @abstractmethod
    def all_child_of(self, name_folder: str):
        pass


@dataclass
class RelationshipFolder(RelationshipBrowser):
    relations: ClassVar = []

    def add_parrent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def all_child_of(self, name_folder: str):
        for i in self.relations:
            if i[0].name == name_folder and i[1] == Relationship.PARENT:
                yield i[2].name


def Research(name_folder: str, relations: RelationshipFolder):
    for i in relations.all_child_of(name_folder):
        print(f'Подпапки главного каталога {i}')


if __name__ == '__main__':
    root = Folder('C//:')
    program = Folder('Program')
    window = Folder('Window')

    relation = RelationshipFolder()
    relation.add_parrent_and_child(root, program)
    relation.add_parrent_and_child(root, window)

    Research('C//:', relation)
