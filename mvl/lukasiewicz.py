'''
@author: Andrew J. Young
@description: A base class for Lukasiewicz's 3 valued logic.
'''


from mvl.settings import CLASS_CREATION_THRESHOLD


class LogicValue:
    name = None
    class_name = 'LogicValue'

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return self.__bool__()

    def __init__(self, index, n_values):
        self.index = index
        self.float_ = index / (n_values - 1)
        self.n_values = n_values

    def __bool__(self):
        # This should be implemented by the inheritors of this class.
        raise NotImplementedError('This method should be implemented by child' \
        'classes')

    def __repr__(self):
        if self.name:
            return '{}.{}'.format(self.class_name, self.name)
        else: # self.name is None
            return '{}({} of {})'.format(
                self.class_name,
                self.index,
                self.n_values,
            )

    def __float__(self):
        return self.float_


class LukasiewiczLogicValue(LogicValue):
    class_name = 'LukasiewiczLogicValue'

    def __bool__(self):
        return float(self) == 1


class PriestLogicValue(LogicValue):
    class_name = 'PriestLogicValue'

    def __bool__(self):
        return float(self) != 0


class LogicSystem:
    n_values = None
    values = []

    def __init__(self, n_values, logic_value_class):
        self.n_values = n_values
        self.logic_value_class = logic_value_class

    def gen_classes(self, i_have_read_the_ts_and_cs = False):
        if (self.n_values > CLASS_CREATION_THRESHOLD
            and not i_have_read_the_ts_and_cs
        ):
            print('''
Hello! It seems that you're trying to create a *lot* of classes
right now!

Before you do this, you should check that you really want to create
all of these. Classes take up a lot of space in memory, and may
affect the performance of your code and the rest of your machine.

Before you do this, be sure that this is what you want to do. Better
yet, run tests on what your computer is able to handle. If you're
still sure that you want to create all these classes, rerun this
function with the parameter `i_have_read_the_ts_and_cs = True`.

Happy hacking!
            ''')
            return

        self.values = [
            self.logic_value_class(i, self.n_values)
            for i in range(self.n_values)
        ]

    def mvl(self, f):
        return self.values[int(f * self.n_values) - 1]


def s_and(a, b):
    a = float(a)
    b = float(b)
    return max(0, a + b - 1)


def w_and(a, b):
    a = float(a)
    b = float(b)
    return min(a, b)


def s_or(a, b):
    a = float(a)
    b = float(b)
    return min(1, a + b)


def w_or(a, b):
    a = float(a)
    b = float(b)
    return max(a, b)


def not_(a):
    a = float(a)
    return 1 - a


def implies(a, b):
    a = float(a)
    b = float(b)
    return min(1, 1 - a + b)


def equivalent(a, b):
    a = float(a)
    b = float(b)
    return (1 - abs(a - b))

