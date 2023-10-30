from cpython.list cimport PyList_New
from enum import Enum


cdef enum Expect:
    CURLY_BRACKET
    SQUARE_BRACKET
    DOUBLE_QUOTATION
    COLON
    VALUE
    R
    U
    E
    A
    L
    S


cdef dict EXPECT_VALUES = {
    CURLY_BRACKET: '}',
    SQUARE_BRACKET: ']',
    DOUBLE_QUOTATION: '"',
    COLON: ':',
    VALUE: 'null',
    R: 'r',
    U: 'u',
    E: 'e',
    A: 'a',
    L: 'l',
    S: 's'
}

cdef str expect_to_completion(Expect expect):
    return EXPECT_VALUES[expect]


cdef list get_expects(str trunc, list expects=[], char last_char=0):
    cdef list new_expects = list(expects)
    cdef char ch
    for ch in [ord(c) for c in trunc]:
        if last_char == '\\':
            last_char = 0
        else:
            last_char = ch
            if ch == ' ':
                continue
            elif ch == '{':
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
                elif new_expects[-1] == Expect.SQUARE_BRACKET:
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
                elif ch == 'f':
                    new_expects.append(Expect.E)
                    new_expects.append(Expect.S)
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.A)
                elif ch == 'n':
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.L)
                    new_expects.append(Expect.U)
            elif new_expects[-1] in [Expect.R, Expect.U, Expect.E, Expect.A, Expect.L, Expect.S]:
                new_expects.pop()
    return new_expects


cdef str get_completion(list expects=[]):
    return ''.join(map(expect_to_completion, reversed(expects)))


cpdef str complete(str trunc):
    return trunc + get_completion(get_expects(trunc))
