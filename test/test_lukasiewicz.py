# Imports from third party packages.
from unittest import TestCase
from unittest import main as unittest_main

# Imports from the local package.
from mvl.lukasiewicz import (
    LogicValue,
    LogicSystem,
    LukasiewiczLogicValue,
    PriestLogicValue,
)

class TestLogicValue(TestCase):
    class_ = LogicValue
    class_name = 'LogicValue'

    def setUp(self):
        self.index = 3
        self.n_values = 5
        self.float_ = self.index / (self.n_values - 1)
        self.instance = self.class_(self.index, self.n_values)

    def test_eq(self):
        instance = self.instance
        self.assertEqual(instance, self.instance)
        self.assertEqual(instance, self.float_)

    def test_ne(self):
        instance = self.instance
        self.assertNotEqual(instance, self.class_(self.index, self.n_values + 1))
        self.assertNotEqual(instance, self.float_ + 1)

    def test_float(self):
        self.assertEqual(self.float_, float(self.instance))

    def test_bool(self):
        with self.assertRaises(NotImplementedError):
            bool(self.instance)

    def _test_bool(self, expected_truth_vals):
        for i in range(3):
            val = self.class_(i, 3)
            self.assertEqual(expected_truth_vals[i], bool(val))

    def _test_repr_without_name(self, class_name):
        expected = '{}({} of {})'.format(class_name, self.index, self.n_values)
        actual = str(self.instance)

        self.assertEqual(expected, actual)

    def _test_repr_with_name(self, class_name):
        instance = self.class_(self.index, self.n_values)

        # Overwrite the name of the instance
        value_name = 'test_name'
        instance.name = value_name

        expected = '{}.{}'.format(class_name, value_name)
        actual = str(instance)

        self.assertEqual(expected, actual)

    def test_repr_with_name(self):
        self._test_repr_with_name(self.class_name)

    def test_repr_without_name(self):
        self._test_repr_without_name(self.class_name)


class TestLukasiewiczLogicValue(TestLogicValue):
    class_ = LukasiewiczLogicValue
    class_name = 'LukasiewiczLogicValue'

    def test_bool(self):
        expected_truth_vals = [False, False, True]
        self._test_bool(expected_truth_vals)


class TestPriestLogicValue(TestLogicValue):
    class_ = PriestLogicValue
    class_name = 'PriestLogicValue'

    def test_bool(self):
        expected_truth_vals = [False, True, True]
        self._test_bool(expected_truth_vals)


class TestLogicSystem(TestCase):
    def setUp(self):
        self.n_values = 5
        self.logic_value_class = LukasiewiczLogicValue

    def _logic_system(self):
        return LogicSystem(self.n_values, self.logic_value_class)

    def test_gen_classes_with_reading_ts_and_cs(self):
        ## Setup ###############################################################

        n_values = self.n_values

        logic_system = self._logic_system()

        ## Execution ###########################################################

        logic_system.gen_classes()

        ## Assertion ###########################################################

        # Assert <n_values> logic values have been added.
        self.assertEqual(n_values, len(logic_system.values))


if __name__ == '__main__':
    unittest_main()
