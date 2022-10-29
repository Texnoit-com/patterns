from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Register:
    entries: ClassVar = []
    count: ClassVar = 0

    def __str__(self) -> str:
        '''Вывод всех записей'''
        return '\n'.join(self.entries)

    def add_entry(self, entry: str) -> None:
        '''Добавление записей'''
        self.count += 1
        self.entries.append(f'{self.count} - {entry}')

    def remove_entry(self, pos: int) -> None:
        '''Удаление записей'''
        del self.entries[pos]


class SaveManager:
    '''Класс сохранения регистра в файл'''
    @staticmethod
    def save_to_file(register, filename) -> None:
        file = open(filename, 'w')
        file.write((str(register)))
        file.close()


if __name__ == '__main__':
    reg = Register()
    reg.add_entry('Добавление файла hello')
    reg.add_entry('Изменение файла hello')

    file = r'C:\temp\Register.txt'
    SaveManager.save_to_file(reg, file)

    with open(file) as f:
        print(f.read())
