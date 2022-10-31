from dataclasses import dataclass
from typing import ClassVar


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
@dataclass
class Database:
    name: str

    def __post_init__(cls):
        print(cls.name)


if __name__ == '__main__':
    d1 = Database('SQL')
    d2 = Database('NOSQL')

    print(d1 == d2)
    print(d2.name)
