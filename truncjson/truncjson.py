from typing import List
from enum import Enum


class Expect(Enum):
    CURLY_BRACKET = '}'
    SQUARE_BRACKET = ']'
    DOUBLE_QUOTATION = '"'
    COLON = ':'
    VALUE = 'null'
    R = 'r'
    U = 'u'
    E = 'e'
    A = 'a'
    L = 'l'
    S = 's'


def expect_to_completion(expect: Expect) -> str:
    return expect.value


def get_expects(trunc: str, expects: List[Expect] = [], last_char: int = 0) -> List[Expect]:
    new_expects = list(expects)
    for ch in trunc:
        if last_char == ord('\\'):
            last_char = 0
        else:
            last_char = ord(ch)
            if ch == '{':
                if len(new_expects) > 0:
                    if new_expects[-1] == Expect.VALUE:
                        new_expects.pop()
                new_expects.append(Expect.CURLY_BRACKET)
            elif ch == '[':
                if len(new_expects) > 0:
                    if new_expects[-1] == Expect.VALUE:
                        new_expects.pop()
                new_expects.append(Expect.SQUARE_BRACKET)
            elif ch == ',':
                if new_expects[-1] == Expect.SQUARE_BRACKET:
                    new_expects.append(Expect.VALUE)
                else:
                    new_expects.append(Expect.VALUE)
                    new_expects.append(Expect.COLON)
                    new_expects.append(Expect.DOUBLE_QUOTATION)
                    new_expects.append(Expect.DOUBLE_QUOTATION)
            elif ch == '"':
                if new_expects[-1] == Expect.DOUBLE_QUOTATION:
                    new_expects.pop()
                elif new_expects[-1] == Expect.VALUE:
                    new_expects.pop()
                    new_expects.append(Expect.DOUBLE_QUOTATION)
                else:
                    new_expects.append(Expect.VALUE)
                    new_expects.append(Expect.COLON)
                    new_expects.append(Expect.DOUBLE_QUOTATION)
            elif ch == ':':
                assert new_expects.pop() == Expect.COLON
            elif ch == ']':
                assert new_expects.pop() == Expect.SQUARE_BRACKET
            elif ch == '}':
                assert new_expects.pop() == Expect.CURLY_BRACKET
            elif new_expects[-1] == Expect.VALUE:
                new_expects.pop()
                if ch == 't':
                    new_expects.append(Expect.E)
                    new_expects.append(Expect.U)
                    new_expects.append(Expect.R)
                if ch == 'f':
                    new_expects.append(Expect.E)
                    new_expects.append(Expect.S)
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.A)
                if ch == 'n':
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.U)
            elif new_expects[-1] in [Expect.R, Expect.U, Expect.E, Expect.A, Expect.L, Expect.S]:
                new_expects.pop()
    return new_expects


def get_completion(expects: List[Expect] = []) -> str:
    return ''.join(map(expect_to_completion, reversed(expects)))


def complete(trunc: str) -> str:
    return trunc + get_completion(get_expects(trunc))
