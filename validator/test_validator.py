import unittest
from validator.validator import Validator


class TestValidator(unittest.TestCase):

    def test_execute_user_input(self):
        validator = Validator([])
        validator.execute_user_input()
