'''
@author: Andrew J. Young
@description: A base class for Priest's 3 valued logic.
'''

from mvl.lukasiewicz import PriestLogicValue, LogicSystem

## Begin system setup ##########################################################

priest = LogicSystem(3, PriestLogicValue)
priest.gen_classes(i_have_read_the_ts_and_cs = True)

f = priest.values[0]
u = priest.values[1]
t = priest.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

############################################################ End system setup ##
## Begin logical operators #####################################################

from mvl.lukasiewicz import not_
from mvl.lukasiewicz import w_and as and_
from mvl.lukasiewicz import w_or as or_

iff = lambda a, b: and_(implies(a, b), implies(b, a))
xor = lambda a, b: not_( iff( a, b ))
implies = lambda a, b: or_( not_( a ), b )

####################################################### End logical operators ##

