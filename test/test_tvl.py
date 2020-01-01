'''
@author: Andrew J. Young
@description: Unit tests for kleene 3 valued logic.
'''


# Imports from third party packages.
from unittest import main as unittest_main
from unittest import TestCase

# Imports from the local package.
import mvl.bochvar as bochvar
import mvl.kleene as kleene
import mvl.priest as priest


## Begin test template classes #################################################


class TVLTestCase():
    def _setUp(self):
        mvl = self.mvl

        self.f = mvl.f
        self.u = mvl.u
        self.t = mvl.t

        self.vals = [self.f, self.u, self.t]

class TVLCoreTests(TVLTestCase):
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


class TVLOperatorTests(TVLTestCase):
    def _test_binary_operator(self, op, expected_truth_table):
        f = self.f
        u = self.u
        t = self.t

        actual_truth_table = [
            # f        u         t
            [op(f, f), op(f, u), op(f, t)], # f
            [op(u, f), op(u, u), op(u, t)], # u
            [op(t, f), op(t, u), op(t, t)], # t
        ]

        for i in range(len(expected_truth_table)):
            for j in range(len(expected_truth_table[0])):
                self.assertEqual(expected_truth_table[i][j],
                    actual_truth_table[i][j]
                )

    def _test_unary_operator(self, op, expected_truth_table):
        actual_truth_table = [
            op(self.f), # f
            op(self.u), # u
            op(self.t), # t
        ]

        for i in range(len(expected_truth_table)):
            self.assertEqual(expected_truth_table[i], actual_truth_table[i])

    def test_not_(self):
        expected_truth_table = [
            self.t, # f
            self.u, # u
            self.f, # t
        ]
        self._test_unary_operator(self.mvl.not_, expected_truth_table)

    def test_iff(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ t, u, f], # f
            [ u, u, u], # u
            [ f, u, t], # t
        ]
        self._test_binary_operator(self.mvl.iff, expected_truth_table)


class KleenePriestOperatorTests(TVLOperatorTests):
    def test_and_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ f, f, f], # f
            [ f, u, u], # u
            [ f, u, t], # t
        ]
        self._test_binary_operator(self.mvl.and_, expected_truth_table)

    def test_or_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ f, u, t], # f
            [ u, u, t], # u
            [ t, t, t], # t
        ]
        self._test_binary_operator(self.mvl.or_, expected_truth_table)

    def test_xor(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ f, u, t], # f
            [ u, u, u], # u
            [ t, u, f], # t
        ]
        self._test_binary_operator(self.mvl.xor, expected_truth_table)

    def test_implies(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ t, t, t], # f
            [ u, u, t], # u
            [ f, u, t], # t
        ]
        self._test_binary_operator(self.mvl.implies, expected_truth_table)


class BochvarOperatorsTests(TVLOperatorTests):
    def test_and_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ f, u, f], # f
            [ u, u, u], # u
            [ f, u, t], # t
        ]
        self._test_binary_operator(self.mvl.and_, expected_truth_table)

    def test_or_(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ f, u, t], # f
            [ u, u, u], # u
            [ t, u, t], # t
        ]
        self._test_binary_operator(self.mvl.or_, expected_truth_table)

    def test_implies(self):
        f = self.f
        u = self.u
        t = self.t

        expected_truth_table = [
            # f  u  t
            [ t, u, t], # f
            [ u, u, u], # u
            [ f, u, t], # t
        ]
        self._test_binary_operator(self.mvl.implies, expected_truth_table)


################################################### End test template classes ##
## Begin test classes ##########################################################


class TestKleeneCore(TVLCoreTests, TestCase):
    def setUp(self):
        self.mvl = kleene
        self._setUp()

    def test_bool_eval(self):
        expected = {
            str(self.f): False,
            str(self.u): False,
            str(self.t): True,
        }

        for val in self.vals:
            self._test_bool_eval(val, expected[str(val)])


class TestKleeneOperators(KleenePriestOperatorTests, TestCase):
    def setUp(self):
        self.mvl = kleene
        self._setUp()


class TestBochvarCore(TestKleeneCore, TestCase):
    def setUp(self):
        self.mvl = bochvar
        self._setUp()


class TestBochvarOperators(BochvarOperatorsTests, TestCase):
    def setUp(self):
        self.mvl = bochvar
        self._setUp()


class TestPriestCore(TVLCoreTests, TestCase):
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


class TestPriestOperators(KleenePriestOperatorTests, TestCase):
    def setUp(self):
        self.mvl = priest
        self._setUp()


############################################################ End test classes ##


if __name__ == '__main__':
    unittest_main()

