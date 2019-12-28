# Imports from third party packages.
from unittest import main as unittest_main
from unittest import TestCase

# Imports from the local package.
import tvl.kleene as tvl

U = tvl.U()
T = tvl.T()
F = tvl.F()


class TestLogicValue(TestCase):
    def _test_int_eval(self, expected):
        actual = int(self.val)
        self.assertEqual(expected, actual)

    def _test_bool_eval(self, expected):
        actual = bool(self.val)
        self.assertEqual(expected, actual)


class TestKleeneF(TestLogicValue):
    def setUp(self):
        self.val = F

    def test_bool_eval(self):
        self._test_bool_eval(False)

    def test_int_eval(self):
        self._test_int_eval(-1)


class TestKleeneU(TestLogicValue):
    def setUp(self):
        self.val = U

    def test_bool_eval(self):
        self._test_bool_eval(False)

    def test_int_eval(self):
        self._test_int_eval(0)


class TestKleeneT(TestLogicValue):
    def setUp(self):
        self.val = T

    def test_bool_eval(self):
        self._test_bool_eval(True)

    def test_int_eval(self):
        self._test_int_eval(1)


class TestOperators(TestCase):
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
        self._test_binary_operator(tvl.and_, expected_truth_table)

    def test_or_(self):
        expected_truth_table = [
            # U  T  F
            [ U, T, U], # U
            [ T, T, T], # T
            [ U, T, F], # F
        ]
        self._test_binary_operator(tvl.or_, expected_truth_table)

    def test_xor(self):
        expected_truth_table = [
            # U  T  F
            [ U, U, U], # U
            [ U, F, T], # T
            [ U, T, F], # F
        ]
        self._test_binary_operator(tvl.xor, expected_truth_table)

    def test_iff(self):
        expected_truth_table = [
            # U  T  F
            [ U, U, U], # U
            [ U, T, F], # T
            [ U, F, T], # F
        ]
        self._test_binary_operator(tvl.iff, expected_truth_table)

    #def test_implies(self):
        # TODO: Should throw an error.
        #expected_truth_table = [
        #    # U  T  F
        #    [ U, U, U], # U
        #    [ U, T, F], # T
        #    [ U, F, T], # F
        #]
        #self._test_binary_operator(tvl.iff, expected_truth_table)

    def test_not_(self):
        expected_truth_table = [
            U, # U
            F, # T
            T, # F
        ]
        self._test_unary_operator(tvl.not_, expected_truth_table)


if __name__ == '__main__':
    unittest_main()

