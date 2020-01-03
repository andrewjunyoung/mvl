"""
.. module: kleene
   :synopsis: A module for kleene 3 valued logic.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies


kleene: LogicSystem = LogicSystem(3, LukasiewiczLogicValue)
""" A 3 valued LogicSystem which uses the values «False»; «Unknown»; and «True».
Kleene logic systems are like lukasiewicz logic systems in that «True» is
considered the only truth value.
"""

f: LukasiewiczLogicValue = kleene.values[0]
""" The kleene logic value «False».
"""

u: LukasiewiczLogicValue = kleene.values[1]
""" The kleene logic value «Unknown».
"""

t: LukasiewiczLogicValue = kleene.values[2]
""" The kleene logic value «True».
"""

f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

