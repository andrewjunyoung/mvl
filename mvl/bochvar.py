'''
.. module: bochvar
   :synopsis: A module for bochvar 3 valued logic.

.. moduleauthor: Andrew J. Young
'''


from mvl.lukasiewicz import LogicSystem, LogicValue, LukasiewiczLogicValue


## Begin system setup ##########################################################

bochvar: LogicSystem = LogicSystem(3, LukasiewiczLogicValue)
bochvar.gen_classes(i_have_read_the_ts_and_cs = True)

f: LukasiewiczLogicValue = bochvar.values[0]
u: LukasiewiczLogicValue = bochvar.values[1]
t: LukasiewiczLogicValue = bochvar.values[2]
f.name = 'False'
u.name = 'Unknown'
t.name = 'True'

############################################################ End system setup ##
## Begin logical operators #####################################################

from mvl.tvl_operators import not_, iff

def and_(a, b):
    """
    The and operator used by Bochvar. This operator (and; &) has the truth
    table:

      | f | u | t |
    f | t | u | f |
    u | u | u | u |
    t | f | u | f |

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        (LogicValue) a & b
    """
    if a == u or b == u:
        return u
    return float(bool(a) and bool(b))

def or_(a, b):
    """
    The or operator used by Bochvar. This operator (or; |) has the truth
    table:

      | f | u | t |
    f | t | u | t |
    u | u | u | u |
    t | t | u | f |

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        (LogicValue) a | b
    """
    if a == u or b == u:
        return u
    return float(bool(a) or bool(b))

def implies(a, b):
    """
    The implication operator used by Bochvar. This operator (->; →) has the
    truth table:

      | f | u | t |
    f | t | u | f |
    u | u | u | u |
    t | t | u | t |

    Args:
        a (LogicValue)
        b (LogicValue)

    Returns:
        (LogicValue) a -> b
    """
    if a == u or b == u:
        return u
    return float(bool(b) ** bool(a)) # Equivalent to normal boolean implication.

####################################################### End logical operators ##

