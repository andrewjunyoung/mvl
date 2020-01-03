"""
.. module: Lukasiewicz
   :synopsis: The default classes and methods for building finite valued logic
   systems. Includes the methods for creating Lukasiewicz finite valued logic
   systems.

.. moduleauthor: Andrew J. Young
"""

from typing import List, Callable


from mvl.types import Floatable


class LogicValue:
    """ A representation of a general lukasiewicz-goedel logic value.

    Lukasiewicz and goedel logic values span over the interval [0, 1], and can
    be finite or infinite in length (but for practical reasons, the latter is
    not implemented using classes).

    Attributes:
        name (str): An alternative name for the logic value, used in the
            representation of the class. See __repr__.
        class_name (str): The name of the class, used in its representation. See
            __repr__. Equal to 'LogicValue'
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

    def __init__(self, val: float) -> None:
        self.val: float = val

    @classmethod
    def from_frac(cls, index: int, max_index: int) -> None:
        return cls(index / max_index)

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
            return '{}({})'.format(
                self.class_name,
                self.val
            )

    def __float__(self) -> float:
        return self.val


class LukasiewiczLogicValue(LogicValue):
    """ A type of LogicValue. LukasiewiczLogicValues are considered to be "true"
    (in a 2 valued boolean sense) iff their float representation is 1.

    Attributes:
        name (str): An alternative name for the logic value, used in the
            representation of the class. See __repr__.
        class_name (str): The name of the class, used in its representation. See
            __repr__. Equal to 'LukasiewiczLogicValue'.
    """
    class_name: str = 'LukasiewiczLogicValue'

    def __bool__(self) -> bool:
        return float(self) == 1


class PriestLogicValue(LogicValue):
    """ A type of LogicValue. PriestLogicValues are considered to be "true"
    (in a 2 valued boolean sense) iff their float representation not 0.

    Attributes:
        name (str): An alternative name for the logic value, used in the
            representation of the class. See __repr__.
        class_name (str): The name of the class, used in its representation. See
            __repr__. Equal to 'PriestLogicValue'.
    """
    class_name: str = 'PriestLogicValue'

    def __bool__(self) -> bool:
        return float(self) != 0


class LogicSystem:
    """ A class for creating logical systems and the associated logical values,
    and for converting numerical values into LogicValues.

    Attributes:
        n_values (int): The number of values in the LogicSystem. Equal to
            len(LogicSystem.values).
        values (List[LogicValue]): The ordered list of logic values in the
            logical system.
    """

    n_values: int = 0
    values: List[LogicValue] = []

    def __init__(self, n_values: int, logic_value_class: Callable) -> None:
        self.n_values: int = n_values
        self.logic_value_class: Callable = logic_value_class
        self._gen_classes() # Sets self.values to a list of LogicValues.

    def _gen_classes(self) -> None:
        """ Generates self.n_values LogicValues, in order, for the current
        logical system, and saves these objects in self.values.
        """
        max_index = self.n_values - 1
        self.values: List[LogicValue] = [
            self.logic_value_class.from_frac(i, max_index)
            for i in range(self.n_values)
        ]

    def mvl(self, f: float) -> LogicValue:
        """ Given a float, returns the associated logic value in the current
        system, if one exists. """
        return self.values[int(f * self.n_values) - 1]


def s_and(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «strong and» operator. This operator (&&) is defined by:

    a && b := max {0, a + b - 1}

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a && b
    """
    a = float(a)
    b = float(b)
    return max(0, a + b - 1)



def w_and(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «weak and» operator. This operator (&) is defined by:

    a & b := min {a, b}

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a & b
    """
    a = float(a)
    b = float(b)
    return min(a, b)


def s_or(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «strong or» operator. This operator (||) is defined by:

    a || b := min {1, a + b}

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a || b
    """
    a = float(a)
    b = float(b)
    return min(1, a + b)


def w_or(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «weak or» operator. This operator (|) is defined by:

    a | b := max {a, b}

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a | b
    """
    a = float(a)
    b = float(b)
    return max(a, b)


def not_(a: Floatable) -> float:
    """ Lukasiewicz's «not» operator. This operator (!) is defined by:

    ! a := 1 - a

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: ! a
    """
    a = float(a)
    return 1 - a


def implies(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «implies» operator. This operator (→) is defined by:

    a → b = min {1, 1 - a + b}

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a → b
    """
    a = float(a)
    b = float(b)
    return min(1, 1 - a + b)


def equivalent(a: Floatable, b: Floatable) -> float:
    """ Lukasiewicz's «equivalence» operator. This operator (↔, not to be confused
    with the biconditional «iff») is defined by:

    a ↔ b = 1 - | a - b |

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a ↔ b
    """
    a = float(a)
    b = float(b)
    return (1 - abs(a - b))

