'''
@author: Andrew J. Young
@description: Unit tests for kleene 3 valued logic.
'''


# Imports from third party packages.
from unittest import main as unittest_main
from unittest import TestCase

# Imports from the local package.
import mvl.kleene as kleene
import mvl.priest as priest


class ThreeValuedLogicTests(TestCase):
    def _setUp(self):
        mvl = self.mvl

        self.f = mvl.f
        self.u = mvl.u
        self.t = mvl.t

        self.vals = [self.f, self.u, self.t]

    def setUp(self):
        self.mvl = kleene
        self._setUp()

    def _test_int_eval(self, val, expected):
        actual = float(val)
        self.assertEqual(expected, actual)


    def _test_bool_eval(self, val, expected):
        actual = bool(val)
        self.assertEqual(expected, actual)


    def test_int_eval(self):
        expected = {
            str(self.f): 0,
            str(self.u): 0.5,
            str(self.t): 1,
        }

        for val in self.vals:
            self._test_int_eval(val, expected[str(val)])


    def _test_binary_operator(self, op, expected_truth_table):
        f = self.f
        u = self.u
        t = self.t

        actual_truth_table = [
            # u        t         f
            [op(u, u), op(u, t), op(u, f)], # u
            [op(t, u), op(t, t), op(t, f)], # t
            [op(f, u), op(f, t), op(f, f)], # f
        ]

        for i in range(len(expected_truth_table)):
            for j in range(len(expected_truth_table[0])):
                self.assertEqual(expected_truth_table[i][j],
                    actual_truth_table[i][j]
                )


    def _test_unary_operator(self, op, expected_truth_table):
        actual_truth_table = [
            op(self.u), # u
            op(self.t), # t
            op(self.f), # f
        ]

        for i in range(len(expected_truth_table)):
            self.assertEqual(expected_truth_table[i], actual_truth_table[i])


    def test_and_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # u  t  f
            [ u, u, f], # u
            [ u, t, f], # t
            [ f, f, f], # f
        ]
        self._test_binary_operator(self.mvl.and_, expected_truth_table)


    def test_or_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # u  t  f
            [ u, t, u], # u
            [ t, t, t], # t
            [ u, t, f], # f
        ]
        self._test_binary_operator(self.mvl.or_, expected_truth_table)


    def test_xor(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # u  t  f
            [ u, u, u], # u
            [ u, f, t], # t
            [ u, t, f], # f
        ]
        self._test_binary_operator(self.mvl.xor, expected_truth_table)


    def test_iff(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # u  t  f
            [ u, u, u], # u
            [ u, t, f], # t
            [ u, f, t], # f
        ]
        self._test_binary_operator(self.mvl.iff, expected_truth_table)

    def test_implies(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # u  t  f
            [ u, t, u], # u
            [ u, t, f], # t
            [ t, t, t], # f
        ]
        self._test_binary_operator(self.mvl.implies, expected_truth_table)

    def test_not_(self):
        expected_truth_table = [
            self.u, # u
            self.f, # t
            self.t, # f
        ]
        self._test_unary_operator(self.mvl.not_, expected_truth_table)


class TestKleene(ThreeValuedLogicTests):
    def test_bool_eval(self):
        expected = {
            str(self.f): False,
            str(self.u): False,
            str(self.t): True,
        }

        for val in self.vals:
            self._test_bool_eval(val, expected[str(val)])


class TestPriest(ThreeValuedLogicTests):
    def setUp(self):
        self.mvl = priest
        self._setUp()

    def test_bool_eval(self):
        expected = {
            str(self.f): False,
            str(self.u): True,
            str(self.t): True,
        }

        for val in self.vals:
            self._test_bool_eval(val, expected[str(val)])


if __name__ == '__main__':
    unittest_main()

