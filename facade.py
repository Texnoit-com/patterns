from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TextBuffer:
    width: int = 4
    height: int = 14
    buffer: ClassVar = ['.'] * (width*height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text

    @property
    def read(self):
        return self.buffer


@dataclass
class Viewport:
    buffer: TextBuffer = TextBuffer()
    offset: ClassVar = 0

    def get_char_at(self, index):
        return self.buffer[self.offset+index]

    def append(self, text):
        self.buffer.write(text+' ')

    @property
    def read(self):
        return self.buffer.read


@dataclass
class Console:

    def __post_init__(self):
        b = TextBuffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.append(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)

    @property
    def read(self):
        return self.current_viewport.read


if __name__ == '__main__':
    c = Console()
    c.write('hello')
    c.write('world')
    print(c.read)
    ch = c.get_char_at(28)
    print(ch)
