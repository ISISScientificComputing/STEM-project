import unittest

from stem_project.validator.validator import Validator
from stem_project.validator.function_wrapper import FunctionWrapper


class TestValidator(unittest.TestCase):

    def test_file_input(self):
        validator = Validator(filepath=r'C:\\Users\\mantid\\STEM-project\\stem_project\\test_data\\expected_functions.txt')
        validator.execute_user_input()
        self.assertEqual(validator.right_percentage, 100)
        self.assertEqual(len(validator.hints_functions), 0)

    def test_expected_equal_to_actual(self):
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        collect_data_0 = FunctionWrapper("collect_data", [0])
        set_sample_rotation_0 = FunctionWrapper("set_sample_rotation", [0])
        set_sample_rotation_120 = FunctionWrapper("set_sample_rotation", [120])
        set_sample_rotation_240 = FunctionWrapper("set_sample_rotation", [240])
        set_sample_rotation_360 = FunctionWrapper("set_sample_rotation", [360])
        validator = Validator([[set_sample_rotation_0, set_sample_position_1_1_1],
                               [collect_data_0],
                               [set_sample_rotation_120],
                               [collect_data_0],
                               [set_sample_rotation_240],
                               [collect_data_0],
                               [set_sample_rotation_360]])
        validator.execute_user_input()
        self.assertEqual(validator.right_percentage, 100)
        self.assertEqual(len(validator.hints_functions), 0)

    def test_expected_more_than_actual(self):
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        collect_data_0 = FunctionWrapper("collect_data", [0])
        set_sample_rotation_0 = FunctionWrapper("set_sample_rotation", [0])
        set_sample_rotation_120 = FunctionWrapper("set_sample_rotation", [120])
        set_sample_rotation_240 = FunctionWrapper("set_sample_rotation", [240])
        set_sample_rotation_360 = FunctionWrapper("set_sample_rotation", [360])
        launch_nuke_3_2_1 = FunctionWrapper("launch nuke", [3, 2, 1])
        validator = Validator([[set_sample_position_1_1_1, set_sample_rotation_0],
                               [collect_data_0],
                               [set_sample_rotation_120],
                               [collect_data_0],
                               [set_sample_rotation_240],
                               [collect_data_0],
                               [set_sample_rotation_360],
                               [launch_nuke_3_2_1]])
        validator.execute_user_input()
        self.assertEqual(validator.right_percentage, 87.5)
        self.assertEqual(len(validator.hints_functions), 1)

    def test_expected_less_than_actual(self):
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        set_sample_rotation_0 = FunctionWrapper("set_sample_rotation", [0])
        collect_data_0 = FunctionWrapper("collect_data", [0])
        validator = Validator([[set_sample_position_1_1_1], [set_sample_rotation_0], [collect_data_0]])
        validator.execute_user_input()
        self.assertEqual(validator.right_percentage, 37.5)
        self.assertEqual(len(validator.hints_functions), 5)

    def test_expected_different_arguments_actual(self):
        set_sample_position_1_2_3 = FunctionWrapper("set_sample_position", [1, 2, 3])
        set_sample_rotation_6 = FunctionWrapper("set_sample_rotation", [6])
        set_sample_rotation_420 = FunctionWrapper("set_sample_rotation", [420])
        set_sample_rotation_9000 = FunctionWrapper("set_sample_rotation", [9000])
        set_sample_rotation_7 = FunctionWrapper("set_sample_rotation", [7])
        collect_data_9 = FunctionWrapper("collect_data", [9])
        collect_data_420 = FunctionWrapper("collect_data", [420])
        collect_data_24 = FunctionWrapper("collect_data", [24])
        validator = Validator([[set_sample_position_1_2_3], [set_sample_rotation_6],
                               [collect_data_9], [set_sample_rotation_420],
                               [collect_data_420], [set_sample_rotation_9000],
                               [collect_data_24], [set_sample_rotation_7]])
        validator.execute_user_input()
        self.assertEqual(validator.right_percentage, 0)
        self.assertEqual(len(validator.hints_functions), 8)
