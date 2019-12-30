'''
@author: Andrew J. Young
@description: A base class for Priest's 3 valued logic.
'''

from mvl.kleene import *
# We want to overwrite the definition for U, so delete the existing definition.
del globals()['U']

class U(LogicValue):
    def __int__(self):
        return 0

    def __bool__(self):
        return True # In Priest's 3VL, "True" and "Unknown" are truth values.

    def __repr__(self):
        return '3VL.Unknown'

U = U()
