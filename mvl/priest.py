'''
@author: Andrew J. Young
@description: A base class for Priest's 3 valued logic.
'''

# Imports from the local package.
from mvl.lukasiewicz import PriestLogicValue, LogicSystem
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies

priest = LogicSystem(3, PriestLogicValue)
priest.gen_classes(i_have_read_the_ts_and_cs = True)

f = priest.values[0]
u = priest.values[1]
t = priest.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

