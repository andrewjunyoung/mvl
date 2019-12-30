'''
@author: Andrew J. Young
@description: A base class for Lukasiewicz's 3 valued logic.
'''

class LogicValue:
    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __nonzero__(self):
        return self.__bool__()


class F(LogicValue):
    def __int__(self):
        return -1

    def __bool__(self):
        return False

    def __repr__(self):
        return '3VL.False'


class U(LogicValue):
    def __int__(self):
        return 0

    def __bool__(self):
        return False # In Kleene's 3VL, "True" is the only truth value.

    def __repr__(self):
        return '3VL.Unknown'


class T(LogicValue):
    def __int__(self):
        return 1

    def __bool__(self):
        return True

    def __repr__(self):
        return '3VL.True'


def bool_(a):
    return a == 1


def not_(a):
    return tvl(1 - a)


def s_and(a, b):
    """ "Strong and" operator.
    """
    return tvl(max(0, int(a) + int(b) - 1))


def w_and(a, b):
    """ "Weak and" operator.
    |   | U | T | F |
    | U | U | U | F |
    | T | U | T | F |
    | F | F | F | F |
    """
    return tvl(min(int(a), int(b)))


def s_or(a, b):
    """ "Strong or" operator, equivalent to xor.
    |   | U | T | F |
    | U | U | U | F |
    | T | U | T | F |
    | F | F | F | F |
    """
    return tvl(max(int(a), int(b)))


def w_or(a, b):
    """ "Weak or" operator, equivalent to (inclusive) "or".
    """
    if a == b and b == 0:
        return T
    return max(a, b)


def iff(a, b):
    return int(a) * int(b)


def implies(a, b):
    return tvl(min(1, 1 - a + b))


T = T()
U = U()
F = F()

