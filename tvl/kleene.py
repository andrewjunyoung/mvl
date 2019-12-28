'''
@author: Andrew J. Young
@description: A base class for implementing 3 valued logic.
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


def _is_f(a):
    return (
        a == 'F'
        or a == 'f'
        or a == '-'
        or a == '-1'
        or a == -1
    )


def _is_u(a):
    return (
        a == 'U'
        or a == 'u'
        or a == '?'
        or a == '#'
        or a == '0'
        or a == 0
    )


def is_t(a):
    return (
        a == 'T'
        or a == 't'
        or a == '+'
        or a == '1'
        or a == '+1'
        or a == 1
    )


def tvl(a):
    if _is_f(a):
        return F()
    elif _is_u(a):
        return U()
    elif _is_t(a):
        return T()

    raise ValueError('Failed to convert {} to Kleene 3VL.'.format(a))


def and_(a, b):
    return min(int(a), int(b))


def or_(a, b):
    return max(int(a), int(b))


def not_(a):
    return - int(a)


def iff(a, b):
    return int(a) * int(b)


def xor(a, b):
    return not_(iff(a, b))


def implies(a, b):
    return or_(not_(a), b)

