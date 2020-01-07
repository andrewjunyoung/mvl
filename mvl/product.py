"""
.. module: product
   :synopsis: The operators and objects used in product logics

.. moduleauthor: Andrew J. Young
"""

from mvl.types import Floatable
from mvl.lukasiewicz import (
    LogicValue,
    LogicSystem,
    LukasiewiczLogicValue,
    PriestLogicValue,
)


def mult(a: Floatable, b: Floatable) -> float:
    """ One of the 2 «conjunction» operators provided in product logic (*),
    defined by:

    a * b := ab

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a * b
    """
    return a * b

def implies(a: Floatable, b: Floatable) -> float:
    """ The «implied» operator provided in product logic (→), defined by:

    a → b :=
      | 1      if a <= b
      | b / a  otherwise

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a * b
    """
    if a > b:
        return b / a
    return 1

def not_(a: Floatable) -> float:
    """ The «not» operator provided in product logic (!), defined by:

    ! a := a → 0

    Because ∀a .[a >= 0] this function is equivalent to float(a == 0), and is
    implemented as such.

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: ! a (≡ a → b)
    """
    return float(a == 0)

def and_(a: Floatable, b: Floatable) -> float:
    """ One of the 2 «conjunction» operators provided in product logic (&),
    defined by:

    a & b := a * (a → b)

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a & b (≡ a * (a → b))
    """
    return mult(a, implies(a, b))

