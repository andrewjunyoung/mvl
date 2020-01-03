"""
.. module: kleene
   :synopsis: A module for kleene 3 valued logic.

.. moduleauthor: Andrew J. Young
"""

# Imports from the local package.
from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies


kleene: LogicSystem = LogicSystem(3, LukasiewiczLogicValue)
kleene.gen_classes()

f: LukasiewiczLogicValue = kleene.values[0]
u: LukasiewiczLogicValue = kleene.values[1]
t: LukasiewiczLogicValue = kleene.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

