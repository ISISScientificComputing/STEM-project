import unittest
from stem_project.validator.function_block import FunctionBlock
from stem_project.validator.function_wrapper import FunctionWrapper


class TestFunctionBlock(unittest.TestCase):
    def test_FunctionBlock_with_two_of_same_functions(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_sample_rotation", [10])
        function_block = FunctionBlock([my_function_wrapper_1, my_function_wrapper_2])
        self.assertEqual(len(function_block.efficient_function_wrappers), 1)

    def test_FunctionBlock_with_three_of_same_functions(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_3 = FunctionWrapper("set_sample_rotation", [10])
        function_block = FunctionBlock([my_function_wrapper_1, my_function_wrapper_2, my_function_wrapper_3])
        self.assertEqual(len(function_block.efficient_function_wrappers), 1)

    def test_FunctionBlocks_with_two_different_functions(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_3 = FunctionWrapper("set_sample_position", [1, 1, 1])
        my_function_wrapper_4 = FunctionWrapper("set_sample_position", [1, 1, 1])
        function_block = FunctionBlock([my_function_wrapper_1, my_function_wrapper_2, my_function_wrapper_3,
                                        my_function_wrapper_4])
        self.assertEqual(len(function_block.efficient_function_wrappers), 2)

    def test_FunctionBlocks_with_three_different_functions(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_beam_rotation", [20])
        my_function_wrapper_3 = FunctionWrapper("set_sample_position", [0, 0, 0])
        function_block = FunctionBlock([my_function_wrapper_1, my_function_wrapper_2, my_function_wrapper_3])
        self.assertEqual(len(function_block.efficient_function_wrappers), 3)

    def test_init_valid_input(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        self.assertEqual(type(my_function_wrapper_1), FunctionWrapper)

    def test_init_invalid_input(self):
        not_function_wrapper = [("set_sample_rotation", [10])]
        self.failUnlessRaises(RuntimeError, FunctionBlock, not_function_wrapper)

    def test_valid_equality(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_sample_rotation", [10])
        function_block_1 = FunctionBlock([my_function_wrapper_1])
        function_block_2 = FunctionBlock([my_function_wrapper_2])
        self.assertEqual(function_block_1, function_block_2)

    def test_valid_inequality(self):
        my_function_wrapper_1 = FunctionWrapper("set_sample_rotation", [10])
        my_function_wrapper_2 = FunctionWrapper("set_sample_position", [1, 1, 1])
        function_block_1 = FunctionBlock([my_function_wrapper_1])
        function_block_2 = FunctionBlock([my_function_wrapper_2])
        self.assertNotEqual(function_block_1, function_block_2)
