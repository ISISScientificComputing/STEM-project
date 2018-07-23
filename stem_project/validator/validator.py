from stem_project.validator.function_wrapper import FunctionWrapper
from os.path import isfile
from stem_project.validator.function_block import FunctionBlock


class Validator(object):

    def __init__(self, input_list=None, filepath=None):
        if input_list is None and filepath is None:
            raise RuntimeError("Input is invalid")
        if input_list is not None and filepath is not None:
            raise RuntimeError("Input is invalid")
        if input_list is not None and filepath is None:
            self.expected_functions = input_list
        if input_list is None and filepath is not None:
            self.expected_functions = []
            self.file_path = filepath
            self.does_file_exist_in_dir()
            self.read_expected_from_file()

        self.execution_output_message = []
        self.user_functions = []
        self.percentage_correct = 0

    def does_file_exist_in_dir(self):
        return isfile(self.file_path)

    def read_expected_from_file(self):
        f = open(self.file_path, "r")
        for line in f:
            words = line.split()
            function_block = []
            while words:
                function_name = words[0]
                # remove first item from words list
                words.remove(words[0])
                # Add line that splits up a string where there are commas
                arguments = words[0].split(",")

                try:
                    arguments = [int(i) for i in arguments]
                except ValueError:
                    pass
                function_block.append(FunctionWrapper(function_name, arguments))
                words.remove(words[0])
            self.expected_functions.append(FunctionBlock(function_block))

        f.close()

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
                return "%s is the correct function, but does not have the correct parameters." % actual_function_name.name_of_function
            else:
                return "%s is not the correct function." % actual_function_name.name_of_function

    def function_list_length_mismatch(self, function_block):
        """
        If the expected_function list and the user_functions list are not of equal length
        :param current_index: The current index in the list to check
        """
        """
        If the expected_function list and the user_functions list are not of equal length
        :param current_index: The current index in the list to check
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
