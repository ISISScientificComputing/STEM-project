"""
Takes either a list of expected functions, or a file path to a .txt file
containing the expected functions

1 : Parse the expected functions
2 : Execute the users code
3 : Compare the users code and the expected and return improvements / score

"""

from stem_project.validator.parse_expected_func_file import read_expected_from_file
from stem_project.function_models import FunctionBlock


class Validator(object):

    def __init__(self, input_list=None, file_path=None):
        if input_list is None and file_path is None:
            raise RuntimeError("Input is invalid")
        if input_list and file_path:
            raise RuntimeError("Input is invalid")
        if input_list and file_path is None:
            self.expected_functions = input_list
        else:
            self.expected_functions = []
            self.file_path = file_path
            self.expected_functions = read_expected_from_file(self.file_path)

        self.execution_output_message = []
        self.user_functions = []
        self.percentage_correct = 0

    def execute_user_input(self):
        from stem_project.user_script.user_script import IC
        self.user_functions = IC.track_function
        if len(self.user_functions) == 0:
            raise IOError("No user functions found")
        return self.validate_functions()

    def validate_functions(self):
        self.user_functions = self.format_user_functions()

        # Identify shortest list
        max_iterations = len(self.expected_functions)
        min_iterations = len(self.user_functions)

        if len(self.user_functions) > len(self.expected_functions):
            max_iterations = len(self.user_functions)
            min_iterations = len(self.expected_functions)

        # Calculate percentage total
        total = max_iterations * 10

        # Iterate over the longest list
        points = 0
        for index in range(max_iterations):
            # If both lists have an item at this index
            if index < min_iterations:
                if self.expected_functions[index] == self.user_functions[index]:
                    # If the functions are the same
                    points = points + 10
                    self.percentage_correct = (points / total) * 100
                else:
                    # If the functions are different
                    self.percentage_correct = (points / total) * 100
                    return self.incorrect_function(self.expected_functions[index],
                                                   self.user_functions[index])
            else:
                self.percentage_correct = (points / total) * 100
                if max_iterations == len(self.expected_functions):
                    return self.function_list_length_mismatch(self.expected_functions[index])
                else:
                    return self.function_list_length_mismatch(self.user_functions[index])

        self.percentage_correct = (points / total) * 100

        if self.percentage_correct == 100:
            return "Well done all functions were called correctly!"

    def incorrect_function(self, expected_function_block, actual_function_block):
        for index in range(len(expected_function_block.function_wrappers)):
            expected_function_name = expected_function_block.function_wrappers[index]
            actual_function_name = actual_function_block.function_wrappers[index]
            if expected_function_name == actual_function_name:
                return "%s is the correct function, but does not have the correct parameters." % actual_function_name.\
                    name_of_function
            else:
                return "%s is not the correct function." % actual_function_name.name_of_function

    def function_list_length_mismatch(self, function_block):
        """
        If the expected_function list and the user_functions list are not of equal length
        """
        if len(self.expected_functions) > len(self.user_functions):
            output_string = "You are missing this function %s"
        else:
            output_string = "You have too many of this function %s"
        for function_wrapper in function_block.function_wrappers:
            return output_string % function_wrapper.name_of_function

    def format_user_functions(self):
        current_index = 0
        formatted_user_functions = []
        for block in self.expected_functions:
            current_block_length = len(block.function_wrappers)
            user_functions_block = []
            for _ in range(current_block_length):
                if current_index >= len(self.user_functions):
                    return formatted_user_functions
                user_functions_block.append(self.user_functions[current_index])
                current_index += 1
            formatted_user_functions.append(FunctionBlock(user_functions_block))
        for index in range(current_index, len(self.user_functions)):
            formatted_user_functions.append(FunctionBlock([self.user_functions[index]]))
        return formatted_user_functions
