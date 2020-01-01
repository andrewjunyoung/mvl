'''
@author: Andrew J. Young
@description: A set of basic logical operators for 3 valued logic.
'''

# Imports from the local package.
from mvl.lukasiewicz import not_
from mvl.lukasiewicz import w_and as and_
from mvl.lukasiewicz import w_or as or_

iff = lambda a, b: and_(implies(a, b), implies(b, a))
xor = lambda a, b: not_( iff( a, b ))
implies = lambda a, b: or_( not_( a ), b )

