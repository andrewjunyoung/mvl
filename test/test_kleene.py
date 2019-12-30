'''
@author: Andrew J. Young
@description: Unit tests for kleene 3 valued logic.
'''


# Imports from third party packages.
from unittest import main as unittest_main
from unittest import TestCase

# Imports from the local package.
import tvl.kleene as tvl
from tvl.kleene import F, U, T


class ThreeValuedLogicTests(TestCase):
    def setUp(self):
        self.vals = [F, U, T]
        self.tvl = tvl


    def _test_int_eval(self, val, expected):
        actual = int(val)
        self.assertEqual(expected, actual)


    def _test_bool_eval(self, val, expected):
        actual = bool(val)
        self.assertEqual(expected, actual)


    def test_int_eval(self):
        expected = {
            str(F): -1,
            str(U): 0,
            str(T): 1,
        }

        for val in self.vals:
            self._test_int_eval(val, expected[str(val)])


    def _test_binary_operator(self, op, expected_truth_table):
        actual_truth_table = [
            # Unknown  True      False
            [op(U, U), op(U, T), op(U, F)], # Unknown
            [op(T, U), op(T, T), op(T, F)], # True
            [op(F, U), op(F, T), op(F, F)], # False
        ]

        for i in range(len(expected_truth_table)):
            for j in range(len(expected_truth_table[0])):
                self.assertEqual(expected_truth_table[i][j],
                    actual_truth_table[i][j]
                )


    def _test_unary_operator(self, op, expected_truth_table):
        actual_truth_table = [
            op(U), # Unknown
            op(T), # True
            op(F), # False
        ]

        for i in range(len(expected_truth_table)):
            self.assertEqual(expected_truth_table[i], actual_truth_table[i])


    def test_and_(self):
        expected_truth_table = [
            # U  T  F
            [ U, U, F], # U
            [ U, T, F], # T
            [ F, F, F], # F
        ]
        self._test_binary_operator(self.tvl.and_, expected_truth_table)


    def test_or_(self):
        expected_truth_table = [
            # U  T  F
            [ U, T, U], # U
            [ T, T, T], # T
            [ U, T, F], # F
        ]
        self._test_binary_operator(self.tvl.or_, expected_truth_table)


    def test_xor(self):
        expected_truth_table = [
            # U  T  F
            [ U, U, U], # U
            [ U, F, T], # T
            [ U, T, F], # F
        ]
        self._test_binary_operator(self.tvl.xor, expected_truth_table)


    def test_iff(self):
        expected_truth_table = [
            # U  T  F
            [ U, U, U], # U
            [ U, T, F], # T
            [ U, F, T], # F
        ]
        self._test_binary_operator(self.tvl.iff, expected_truth_table)

    def test_implies(self):
        expected_truth_table = [
            # U  T  F
            [ U, T, U], # U
            [ U, T, F], # T
            [ T, T, T], # F
        ]
        self._test_binary_operator(self.tvl.implies, expected_truth_table)

    def test_not_(self):
        expected_truth_table = [
            U, # U
            F, # T
            T, # F
        ]
        self._test_unary_operator(self.tvl.not_, expected_truth_table)


def TestKleene(ThreeValuedLogicTests):
    def test_bool_eval(self):
        expected = {
            str(F): False,
            str(U): False,
            str(T): True,
        }

        for val in self.vals:
            self._test_bool_eval(val, expected[str(val)])


if __name__ == '__main__':
    unittest_main()

