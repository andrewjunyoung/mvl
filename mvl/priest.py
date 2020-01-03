"""
.. module: priest
   :synopsis: A module for priest 3 valued logic.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.lukasiewicz import PriestLogicValue, LogicSystem
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies

priest: LogicSystem = LogicSystem(3, PriestLogicValue)
""" A 3 valued LogicSystem which uses the values «False»; «Unknown»; and «True».
Priest logic systems define all non-zero logic values as truth values. «Unknown»
and «True» are both truth values in this 3 valued system. Other than this,
priest logic systems use the same definitions and operators as kleene logic
systems.
"""

f: PriestLogicValue = priest.values[0]
""" The priest logic value «False».
"""

u: PriestLogicValue = priest.values[1]
""" The priest logic value «Unknown».
"""

t: PriestLogicValue = priest.values[2]
""" The priest logic value «True».
"""

f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

