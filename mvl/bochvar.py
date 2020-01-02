'''
@author: Andrew J. Young
@description: A base class for implementing bochvar 3 valued logic.
'''


from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue


## Begin system setup ##########################################################

bochvar = LogicSystem(3, LukasiewiczLogicValue)
bochvar.gen_classes(i_have_read_the_ts_and_cs = True)

f = bochvar.values[0]
u = bochvar.values[1]
t = bochvar.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

############################################################ End system setup ##
## Begin logical operators #####################################################

from mvl.tvl_operators import not_, iff

def and_(a, b):
    if a == u or b == u:
        return u
    return float(bool(a) and bool(b))

def or_(a, b):
    if a == u or b == u:
        return u
    return float(bool(a) or bool(b))

def implies(a, b):
    if a == u or b == u:
        return u
    return float(not(bool(a)) or bool(b)) # Equivalent to normal boolean implication.

####################################################### End logical operators ##

