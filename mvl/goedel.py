"""
.. module: goedel
   :synopsis: The operators and objects used in goedel logics.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.types import Floatable
from mvl.lukasiewicz import (
    LogicValue,
    LogicSystem,
    LukasiewiczLogicValue,
    PriestLogicValue,
)


def and_(a: Floatable, b: Floatable) -> float:
    """ Goedel's «and» operator. This operator (&) is defined by:

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


def or_(a: Floatable, b: Floatable) -> float:
    """ Goedel's «or» operator. This operator (|) is defined by:

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
    """ Goedel's «not» operator. This operator (!) is defined by:

    ! a :=
      | 1  if a == 0
      | 0  otherwise

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: ! a
    """
    a = float(a)
    return float(a == 0)


def implies(a: Floatable, b: Floatable) -> float:
    """ Goedel's «implies» operator. This operator (→) is defined by:

    a → b :=
      | 1  if a <= b
      | b  otherwise

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        LogicValue: a → b
    """
    a = float(a)
    b = float(b)
    if a > b:
        return b
    return 1

