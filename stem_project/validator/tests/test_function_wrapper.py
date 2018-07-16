import unittest
from stem_project.validator.function_wrapper import FunctionWrapper

class TestFunctionWrapper(unittest.TestCase):
    def test_function_name_is_string(self):
        my_function_wrapper = FunctionWrapper("name", [])
        actual = my_function_wrapper.name_of_function
        expected = "name"
        self.assertEqual(actual, expected)
    def test_function_name_is_not_string(self):
        my_function_wrapper = FunctionWrapper(1, [])
        actual = my_function_wrapper.name_of_function
        self.assertIsInstance(actual, str)

