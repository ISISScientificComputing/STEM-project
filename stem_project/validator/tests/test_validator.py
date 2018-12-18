import unittest
import os

from stem_project.function_models.function_block import FunctionBlock
from stem_project.validator.validator import Validator
from stem_project.function_models.function_wrapper import FunctionWrapper
from stem_project.project import ROOT_DIR


class TestValidator(unittest.TestCase):

    def test_file_input(self):
        validator = Validator(file_path=os.path.join(ROOT_DIR, 'test_data', 'expected_functions.txt'))
        validator.execute_user_input()
        self.assertEqual(validator.percentage_correct, 100)

    def test_expected_equal_to_actual(self):
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        set_sample_rotation_0 = FunctionWrapper("set_sample_rotation", [0])
        set_up_block = FunctionBlock([set_sample_position_1_1_1, set_sample_rotation_0])
        collect_data_0 = FunctionBlock([FunctionWrapper("collect_data", [0])])
        set_sample_rotation_120 = FunctionBlock([FunctionWrapper("set_sample_rotation", [120])])
        set_sample_rotation_240 = FunctionBlock([FunctionWrapper("set_sample_rotation", [240])])
        set_sample_rotation_360 = FunctionBlock([FunctionWrapper("set_sample_rotation", [360])])
        validator = Validator([set_up_block,
                               collect_data_0,
                               set_sample_rotation_120,
                               collect_data_0,
                               set_sample_rotation_240,
                               collect_data_0,
                               set_sample_rotation_360])
        output_string = validator.execute_user_input()
        self.assertEqual(output_string, "Well done all functions were called correctly!")
        self.assertEqual(validator.percentage_correct, 100)

    def test_expected_more_than_actual(self):
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        set_sample_rotation_0 = FunctionWrapper("set_sample_rotation", [0])
        set_up_block = FunctionBlock([set_sample_position_1_1_1, set_sample_rotation_0])
        collect_data_0 = FunctionBlock([FunctionWrapper("collect_data", [0])])
        set_sample_rotation_120 = FunctionBlock([FunctionWrapper("set_sample_rotation", [120])])
        set_sample_rotation_240 = FunctionBlock([FunctionWrapper("set_sample_rotation", [240])])
        set_sample_rotation_360 = FunctionBlock([FunctionWrapper("set_sample_rotation", [360])])
        launch_nuke_3_2_1 = FunctionBlock([FunctionWrapper("launch nuke", [3, 2, 1])])
        validator = Validator([set_up_block,
                               collect_data_0,
                               set_sample_rotation_120,
                               collect_data_0,
                               set_sample_rotation_240,
                               collect_data_0,
                               set_sample_rotation_360,
                               launch_nuke_3_2_1])
        output_string = validator.execute_user_input()
        self.assertEqual(output_string, "You are missing this function launch nuke")
        self.assertEqual(validator.percentage_correct, 87.5)

    def test_expected_less_than_actual(self):
        set_sample_position_1_1_1 = FunctionBlock([FunctionWrapper("set_sample_position", [1, 1, 1])])
        set_sample_rotation_0 = FunctionBlock([FunctionWrapper("set_sample_rotation", [0])])
        collect_data_0 = FunctionBlock([FunctionWrapper("collect_data", [0])])
        validator = Validator([set_sample_position_1_1_1, set_sample_rotation_0, collect_data_0])
        validator.execute_user_input()
        output_string = validator.execute_user_input()
        self.assertEqual(output_string, "You have too many of this function set_sample_rotation")
        self.assertEqual(validator.percentage_correct, 37.5)

    def test_expected_different_arguments_actual(self):
        set_sample_position_1_2_3 = FunctionBlock([FunctionWrapper("set_sample_position", [1, 2, 3])])
        set_sample_rotation_6 = FunctionBlock([FunctionWrapper("set_sample_rotation", [6])])
        set_sample_rotation_420 = FunctionBlock([FunctionWrapper("set_sample_rotation", [420])])
        set_sample_rotation_9000 = FunctionBlock([FunctionWrapper("set_sample_rotation", [9000])])
        set_sample_rotation_7 = FunctionBlock([FunctionWrapper("set_sample_rotation", [7])])
        collect_data_9 = FunctionBlock([FunctionWrapper("collect_data", [9])])
        collect_data_420 = FunctionBlock([FunctionWrapper("collect_data", [420])])
        collect_data_24 = FunctionBlock([FunctionWrapper("collect_data", [24])])
        validator = Validator([set_sample_position_1_2_3, set_sample_rotation_6,
                               collect_data_9, set_sample_rotation_420,
                               collect_data_420, set_sample_rotation_9000,
                               collect_data_24, set_sample_rotation_7])
        validator.execute_user_input()
        output_string = validator.execute_user_input()
        self.assertEqual(output_string, "set_sample_position is not the correct function.")
        self.assertEqual(validator.percentage_correct, 0)
