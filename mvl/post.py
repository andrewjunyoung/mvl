"""
.. module: post
   :synopsis: The operators and objects used in post logics.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.lukasiewicz import (
    LogicValue,
    LogicSystem,
    LukasiewiczLogicValue,
    PriestLogicValue,
)
from mvl.goedel import and_, or_


class PostLukasiewiczLogicValue(LukasiewiczLogicValue):
    class_name: str = 'PostLukasiewiczLogicValue'

    def __init__(self, index: int, max_index: int) -> None:
        self.index = index
        self.max_index = max_index
        self.val = index / max_index

    @classmethod
    def from_frac(cls, index: int, max_index: int) -> None:
        return cls(index, max_index)


class PostPriestLogicValue(PriestLogicValue):
    class_name: str = 'PostPriestLogicValue'

    def __init__(self, index: int, max_index: int) -> None:
        self.index = index
        self.max_index = max_index
        self.val = index / max_index

    @classmethod
    def from_frac(cls, index: int, max_index: int) -> None:
        return cls(index, max_index)


def not_(a: LogicValue) -> float:
    """ Post's «not» operator (!), defined by:

    ! a :=
      | 1                if a == 0
      | a - 1 / (m - 1)  otherwise

    where m is the number of logic values in the system.

    There are a few things to note about this operator, as it behaves
    differently to other functions in the MVL package. Because of this, you need
    to use it a little differently too.

    Unlike the other MVL modules, post.not_ will *not* work on floats. It will
    *only* work when it is provided with a valid LogicValue.

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: ! a
    """
    if a == 0:
        return 1
    return float(a) - (1 / a.max_index)

