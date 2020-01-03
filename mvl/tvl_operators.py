"""
.. module: 3 valued logic operators
   :synopsis: Logical operators used in kleene and priest 3 valued logic
   systems.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.lukasiewicz import not_
from mvl.lukasiewicz import w_and as and_
from mvl.lukasiewicz import w_or as or_

iff = lambda a, b: and_(implies(a, b), implies(b, a))
"""
The bicondition operator used by Kleene and Priest. This operator (<->; ↔) has
the truth table:

+---+---+---+---+---+
|       |     a     |
+ a ↔ b +---+---+---+
|       | f | u | t |
+===+===+===+===+===+
|   | f | t | u | f |
+   +---+---+---+---+
| b | u | u | u | u |
+   +---+---+---+---+
|   | t | f | u | t |
+---+---+---+---+---+

Args:
    a (LogicValue)
    b (LogicValue)

Returns:
    LogicValue: a ↔ b
"""

xor = lambda a, b: not_(iff(a, b))
"""
The xor operator used by Kleene and Priest. This operator has the truth table:

+---+-----+---+---+---+
|         |     a     |
+ a xor b +---+---+---+
|         | f | u | t |
+===+=====+===+===+===+
|   | f   | f | u | t |
+   +-----+---+---+---+
| b | u   | u | u | u |
+   +-----+---+---+---+
|   | t   | t | u | f |
+---+-----+---+---+---+

Args:
    a (LogicValue)
    b (LogicValue)

Returns:
    LogicValue: a xor b
"""

implies = lambda a, b: or_(not_(a), b)
"""
The implication operator used by Kleene and Priest. This operator (->; →) has
the truth table:

+---+---+---+---+---+
|       |     a     |
+ a → b +---+---+---+
|       | f | u | t |
+===+===+===+===+===+
|   | f | t | t | t |
+   +---+---+---+---+
| b | u | u | u | t |
+   +---+---+---+---+
|   | t | f | u | t |
+---+---+---+---+---+

Args:
    a (LogicValue)
    b (LogicValue)

Returns:
    LogicValue: a → b
"""
