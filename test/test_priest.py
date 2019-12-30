'''
@author: Andrew J. Young
@description: Unit tests for priest's 3 valued logic.
'''

# Imports from third party packages.
from unittest import main as unittest_main

# Imports from the local package.
from test.test_kleene import ThreeValuedLogicTests
import mvl.priest as mvl
from mvl.priest import F, U, T


class TestPriest(ThreeValuedLogicTests):
    def setUp(self):
        self.vals = [F, U, T]
        self.mvl = mvl


    def test_bool_eval(self):
        expected = {
            str(F): False,
            str(U): True,
            str(T): True,
        }

        for val in self.vals:
            self._test_bool_eval(val, expected[str(val)])


if __name__ == '__main__':
    unittest_main

