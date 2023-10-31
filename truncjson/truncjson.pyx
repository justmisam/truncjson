from cpython.list cimport PyList_New
from enum import Enum


cdef enum Expect:
    SEPARATOR
    CURLY_BRACKET
    SQUARE_BRACKET
    DOUBLE_QUOTATION
    COLON
    VALUE
    DIGIT
    R
    U
    E
    A
    L
    S


cdef list EXPECT_VALUES = ['', '}', ']', '"', ':', 'null', '0', 'r', 'u', 'e', 'a', 'l', 's']

cdef str expect_to_completion(int expect):
    if expect < 0:
        return ''
    return EXPECT_VALUES[expect]


cdef list get_expects(str trunc, list expects=[], char last_char=0):
    cdef list separators = []
    cdef list new_expects = list(expects)
    cdef int i = 0
    cdef char ch
    for ch in [ord(c) for c in trunc]:
        if last_char == '\\':
            last_char = 0
        else:
            last_char = ch
            if ch in [' ', '\n', '\t', '\r']:
                i -= 1
                continue
            elif ch == '{':
                if len(new_expects) > 0:
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        if new_expects[-1] in [Expect.VALUE, Expect.DIGIT]:
                            new_expects.pop()
                        new_expects.append(Expect.CURLY_BRACKET)
                else:
                    separators.append(i)
                    i = 1
                    new_expects.append(Expect.CURLY_BRACKET)
            elif ch == '[':
                if len(new_expects) > 0:
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        if new_expects[-1] in [Expect.VALUE, Expect.DIGIT]:
                            new_expects.pop()
                        new_expects.append(Expect.SQUARE_BRACKET)
                else:
                    separators.append(i)
                    i = 1
                    new_expects.append(Expect.SQUARE_BRACKET)
            elif len(new_expects) > 0:
                if ch == ',':
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
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
                    elif new_expects[-1] in [Expect.VALUE, Expect.DIGIT]:
                        new_expects.pop()
                        new_expects.append(Expect.DOUBLE_QUOTATION)
                    elif new_expects[-1] == Expect.SQUARE_BRACKET:
                        new_expects.append(Expect.DOUBLE_QUOTATION)
                    else:
                        new_expects.append(Expect.VALUE)
                        new_expects.append(Expect.COLON)
                        new_expects.append(Expect.DOUBLE_QUOTATION)
                elif ch == '.':
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        new_expects.append(Expect.DIGIT)
                elif ch == ':':
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        assert new_expects.pop() == Expect.COLON
                elif ch == ']':
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        assert new_expects.pop() == Expect.SQUARE_BRACKET
                        if len(new_expects) == 0:
                            separators.append(i)
                            i = 1
                elif ch == '}':
                    if new_expects[-1] != Expect.DOUBLE_QUOTATION:
                        assert new_expects.pop() == Expect.CURLY_BRACKET
                        if len(new_expects) == 0:
                            separators.append(i)
                            i = 1
                elif new_expects[-1] in [Expect.VALUE, Expect.DIGIT]:
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
        i -= 1
    return separators + new_expects


cdef str get_completion(list expects=[]):
    return ''.join(map(expect_to_completion, reversed(expects)))


cpdef str complete(str trunc):
    return trunc + get_completion(get_expects(trunc))
