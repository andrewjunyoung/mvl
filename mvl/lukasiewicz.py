'''
.. module: Lukasiewicz
   :synopsis: The default classes and methods for building finite valued logic
   systems. Includes the methods for creating Lukasiewicz finite valued logic
   systems.

.. moduleauthor: Andrew J. Young
'''

from typing import List, Callable


from mvl.settings import CLASS_CREATION_THRESHOLD
from mvl.types import Floatable


class LogicValue:
    """ A representation of a general lukasiewicz-goedel logic value.

    Lukasiewicz and goedel logic values span over the interval [0, 1], and
    can be finite or infinite in length (but for practical reasons, the latter
    is not implemented using classes).

    Properties:
        name (str): An alternative name for the logic value, used in the
            representation of the class. See __repr__.
        class_name (str): The name of the class, used in its representation. See
            __repr__.
    """
    name: str = ''
    class_name: str = 'LogicValue'

    def __eq__(self, other: Floatable) -> bool:
        """ Logic values are equal iff they are part of the same logical system,
        and have the same numerical representation.
        """
        return float(self) == float(other)

    def __ne__(self, other: object) -> bool:
        """ Returns true iff the two values are not equal.
        """
        return not self.__eq__(other)

    def __nonzero__(self) -> bool:
        return self.__bool__()

    def __init__(self, index: int, n_values: int):
        self.index: int = index
        self.float_: float = index / (n_values - 1)
        self.n_values: int = n_values

    def __bool__(self) -> bool:
        """ Whether or not they are considered to be "true" in a 2 valued
        boolean sense is determined by the implementation of this class.

        Raises:
            NotImplementedError
        """
        raise NotImplementedError('This method should be implemented by child' \
        'classes')

    def __repr__(self) -> str:
        if self.name != '':
            return '{}.{}'.format(self.class_name, self.name)
        else: # self.name is None
            return '{}({} of {})'.format(
                self.class_name,
                self.index,
                self.n_values,
            )

    def __float__(self) -> float:
        return self.float_


class LukasiewiczLogicValue(LogicValue):
    """ A type of LogicValue. LukasiewiczLogicValues are considered to be "true"
    (in a 2 valued boolean sense) iff their float representation is 1.

    Properties:
        class_name (str): 'LukasiewiczLogicValue'
    """
    class_name: str = 'LukasiewiczLogicValue'

    def __bool__(self) -> bool:
        return float(self) == 1


class PriestLogicValue(LogicValue):
    """ A type of LogicValue. PriestLogicValues are considered to be "true"
    (in a 2 valued boolean sense) iff their float representation not 0.

    Properties:
        class_name (str): 'PriestLogicValue'
    """
    class_name: str = 'PriestLogicValue'

    def __bool__(self) -> bool:
        return float(self) != 0


class LogicSystem:
    n_values: int = 0
    values: List[LogicValue] = []

    def __init__(self, n_values: int, logic_value_class: Callable) -> None:
        self.n_values: int = n_values
        self.logic_value_class: Callable = logic_value_class

    def gen_classes(self, i_have_read_the_ts_and_cs: bool = False):
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

        self.values: List[LogicValue] = [
            self.logic_value_class(i, self.n_values)
            for i in range(self.n_values)
        ]

    def mvl(self, f: float) -> LogicValue:
        return self.values[int(f * self.n_values) - 1]


def s_and(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return max(0, a + b - 1)


def w_and(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return min(a, b)


def s_or(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return min(1, a + b)


def w_or(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return max(a, b)


def not_(a: Floatable) -> float:
    a = float(a)
    return 1 - a


def implies(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return min(1, 1 - a + b)


def equivalent(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return (1 - abs(a - b))

