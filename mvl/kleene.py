'''
@author: Andrew J. Young
@description: A base class for implementing kleene 3 valued logic.
'''


from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue


## Begin system setup ##########################################################

kleene = LogicSystem(3, LukasiewiczLogicValue)
kleene.gen_classes(i_have_read_the_ts_and_cs = True)

f = kleene.values[0]
u = kleene.values[1]
t = kleene.values[2]
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

#def _is_f(a):
#    return (
#        a == 'F'
#        or a == 'f'
#        or a == '-'
#        or a == '-1'
#        or a == -1
#    )
#
#
#def _is_u(a):
#    return (
#        a == 'U'
#        or a == 'u'
#        or a == '?'
#        or a == '#'
#        or a == '0'
#        or a == 0
#    )
#
#
#def _is_t(a):
#    return (
#        a == 'T'
#        or a == 't'
#        or a == '+'
#        or a == '1'
#        or a == '+1'
#        or a == 1
#    )
#
