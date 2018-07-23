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

    def test_equality_when_true(self):
        my_function_wrapper_1 = FunctionWrapper("name", [1])
        my_function_wrapper_2 = FunctionWrapper("name", [1])
        self.assertEqual(my_function_wrapper_1, my_function_wrapper_2)

    def test_equality_arg_mismatch(self):
        my_function_wrapper_arg_1 = FunctionWrapper("arguments", [1])
        my_function_wrapper_arg_2 = FunctionWrapper("arguments", [2])
        self.assertNotEqual(my_function_wrapper_arg_1, my_function_wrapper_arg_2)

    def test_equality_name_mismatch(self):
        my_function_wrapper_1 = FunctionWrapper("name", [1])
        my_function_wrapper_2 = FunctionWrapper("names", [1])
        self.assertNotEqual(my_function_wrapper_1, my_function_wrapper_2)

    def test_equality_name_and_arg_mismatch(self):
        my_function_wrapper_1 = FunctionWrapper("name", [1])
        my_function_wrapper_2 = FunctionWrapper("names", [2])
        self.assertNotEqual(my_function_wrapper_1, my_function_wrapper_2)

    def test_greater_than_name_alphabetically_higher(self):
        my_function_wrapper_name_1 = FunctionWrapper("z_name", [1])
        my_function_wrapper_name_2 = FunctionWrapper("name", [1])
        self.assertGreater(my_function_wrapper_name_1, my_function_wrapper_name_2)

    def test_greater_than_name_alphabetically_lower(self):
        my_function_wrapper_name_1 = FunctionWrapper("name", [1])
        my_function_wrapper_name_2 = FunctionWrapper("z_name", [1])
        self.assertGreater(my_function_wrapper_name_2, my_function_wrapper_name_1)

    def test_greater_than_name_equal_args_more(self):
        my_function_wrapper_name_1 = FunctionWrapper("name", [1, 2])
        my_function_wrapper_name_2 = FunctionWrapper("name", [1])
        self.assertGreater(my_function_wrapper_name_1, my_function_wrapper_name_2)

    def test_greater_than_name_equal_args_less(self):
        my_function_wrapper_name_1 = FunctionWrapper("name", [1])
        my_function_wrapper_name_2 = FunctionWrapper("name", [1, 2])
        self.assertGreater(my_function_wrapper_name_2, my_function_wrapper_name_1)
