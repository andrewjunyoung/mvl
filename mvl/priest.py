'''
.. module: priest
   :synopsis: A module for priest 3 valued logic.

.. moduleauthor: Andrew J. Young
'''

# Imports from the local package.
from mvl.lukasiewicz import PriestLogicValue, LogicSystem
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies

priest: LogicSystem = LogicSystem(3, PriestLogicValue)
priest.gen_classes(i_have_read_the_ts_and_cs = True)

f: PriestLogicValue = priest.values[0]
u: PriestLogicValue = priest.values[1]
t: PriestLogicValue = priest.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

