from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, List


@dataclass
class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    type: Type
    text: str

    def __str__(self):
        return f'`{self.text}`'


@dataclass
class Integer:
    value: int


@dataclass
class BinaryOperation:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    type: ClassVar = None
    left: ClassVar = None
    right: ClassVar = None

    @property
    def value(self) -> int:
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


def lex(input: str) -> List[str]:
    result = []
    set_type = {
        '+': Token.Type.PLUS,
        '-': Token.Type.MINUS,
        '(': Token.Type.LPAREN,
        ')': Token.Type.RPAREN
    }
    i = 0
    while i < len(input):
        if input[i] in set_type.keys():
            result.append(Token(set_type[input[i]], input[i]))
        else:
            digits = [input[i]]
            while input[i+1].isdigit():
                digits.append(input[i+1])
                i += 1
            result.append(Token(Token.Type.INTEGER, ''.join(digits)))
        i += 1

    return result


def parse(tokens: List[str]) -> BinaryOperation:
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def eval(input: str) -> None:
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(14+7)-(11+4)')
    eval('12+(13-4)')
