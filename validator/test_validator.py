import unittest
from validator.validator import Validator


class TestValidator(unittest.TestCase):

    def test_execute_user_input(self):
        validator = Validator([("set_sample_position", [1, 1, 1]), ("set_rotation", [0]), ("collect_data", [0])])
        validator.execute_user_input()
