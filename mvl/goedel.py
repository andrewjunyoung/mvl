"""
.. module: Goedel
   :synopsis: The operators and objects used in Goedel logics.

.. moduleauthor: Andrew J. Young
"""

from mvl.lukasiewicz import (
    LogicValue,
    LogicSystem,
    LukasiewiczLogicValue,
    PriestLogicValue,
)

def and_(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return min(a, b)


def or_(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    return max(a, b)


def not_(a: Floatable) -> float:
    a = float(a)
    b = float(b)
    return int(a == 0)


def implies(a: Floatable, b: Floatable) -> float:
    a = float(a)
    b = float(b)
    if a <= b:
        return 1
    return b
