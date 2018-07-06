import unittest
from validator.validator import Validator


class TestValidator(unittest.TestCase):

    def test_expected_equal_to_actual(self):
        validator = Validator([("set_sample_position", [1, 1, 1]), ("set_rotation", [0]), ("collect_data", [0]),
                               ("set_rotation", [120]), ("collect_data", [0]), ("set_rotation", [240]),
                               ("collect_data", [0]), ("set_rotation", [360])])
        validator.execute_user_input()
        self.assertEqual((validator.right_percentage*100), 100)
        self.assertEqual((len(validator.hints_functions)), 0)

    def test_expected_more_than_actual(self):
        validator = Validator([("set_sample_position", [1, 1, 1]), ("set_rotation", [0]), ("collect_data", [0]),
                               ("set_rotation", [120]), ("collect_data", [0]), ("set_rotation", [240]),
                               ("collect_data", [0]), ("set_rotation", [360]), ("launch nuke", [3, 2, 1])])
        validator.execute_user_input()
        self.assertEqual((validator.right_percentage*100), 88.88888888888889)
        self.assertEqual((len(validator.hints_functions)), 1)

    def test_expected_less_than_actual(self):
        validator = Validator([("set_sample_position", [1, 1, 1]), ("set_rotation", [0]), ("collect_data", [0])])
        validator.execute_user_input()
        self.assertEqual((validator.right_percentage * 100), 37.5)
        self.assertEqual((len(validator.hints_functions)), 5)

    def test_expected_different_arguments_actual(self):
        validator = Validator([("set_sample_position", [1, 2, 3]), ("set_rotation", [6]), ("collect_data", [9]),
                               ("set_rotation", [420]), ("collect_data", [420]), ("set_rotation", [9000]),
                               ("collect_data", [24]), ("set_rotation", [7])])
        validator.execute_user_input()
        self.assertEqual((validator.right_percentage * 100), 0)
        self.assertEqual((len(validator.hints_functions)), 8)
