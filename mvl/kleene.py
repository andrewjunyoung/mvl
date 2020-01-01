'''
@author: Andrew J. Young
@description: A base class for implementing kleene 3 valued logic.
'''

# Imports from the local package.
from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue
from mvl.tvl_operators import not_, and_, or_, iff, xor, implies


kleene = LogicSystem(3, LukasiewiczLogicValue)
kleene.gen_classes(i_have_read_the_ts_and_cs = True)

f = kleene.values[0]
u = kleene.values[1]
t = kleene.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

