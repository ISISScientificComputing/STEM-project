from stem_project.validator.function_wrapper import FunctionWrapper
from os.path import isfile


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

        self.hints_functions = []
        self.user_functions = []
        self.points = 0
        self.total = 0

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
            self.expected_functions.append(function_block)

        f.close()

    def execute_user_input(self):
        from stem_project.user_script.user_script import IC
        self.user_functions = IC.track_function
        if len(self.user_functions) == 0:
            raise IOError("No user functions found")
        self.validate_functions()

    def validate_functions(self):
        self.user_functions = create_user_function_blocks(self.user_functions, self.expected_functions)

        # Identify shortest list
        max_iterations = len(self.expected_functions)
        min_iterations = len(self.user_functions)

        if len(self.user_functions) > len(self.expected_functions):
            max_iterations = len(self.user_functions)
            min_iterations = len(self.expected_functions)

        # Calculate percentage total
        self.total = max_iterations*10

        # Iterate over the longest list
        for index in range(max_iterations):
            # If both lists have an item at this index
            if index < min_iterations:
                if compare_function_blocks(self.expected_functions[index], self.user_functions[index]):
                    # If the functions are the same
                    self.points = self.points + 10
                else:
                    # If the functions are different
                    self.incorrect_function(self.expected_functions[index],
                                            self.user_functions[index])
            else:
                if max_iterations == len(self.expected_functions):
                    self.function_list_length_mismatch(self.expected_functions[index])
                else:
                    self.function_list_length_mismatch(self.user_functions[index])

        self.right_percentage = (self.points/self.total)*100

    def incorrect_function(self, expected_function_block, actual_function_block):
        for index in range(len(expected_function_block)):
            expected_function_name = expected_function_block[index]
            actual_function_name = actual_function_block[index]
            if expected_function_name == actual_function_name:
                self.hints_functions.append("%s is the correct function, "
                                            "but does not have the correct parameters." % actual_function_name)
            else:
                self.hints_functions.append("%s is not the correct function." % actual_function_name)

    def function_list_length_mismatch(self, function_block):
        """
        If the expected_function list and the user_functions list are not of equal length
        :param current_index: The current index in the list to check
        """
        if len(self.expected_functions) > len(self.user_functions):
            output_string = "You are missing this function %s"
        else:
            output_string = "You have too many of this function %s"
        for function_wrapper in function_block:
            self.hints_functions.append(output_string %
                                        function_wrapper.name_of_function)




def compare_function_wrappers(function_wrapper_1, function_wrapper_2):
    if function_wrapper_1.name_of_function == function_wrapper_2.name_of_function:
        if function_wrapper_1.list_of_arguments == function_wrapper_2.list_of_arguments:
            return True
    return False


def compare_function_blocks(expected_functions_block, user_functions_block):
        expected_functions = expected_functions_block
        user_functions = user_functions_block
        expected_functions.sort()
        user_functions.sort()
        for index in range(len(expected_functions)):
            if not compare_function_wrappers(expected_functions[index], user_functions[index]):
                return False
        return True


def create_user_function_blocks(all_user_functions, all_expected_functions):
    current_index = 0
    formatted_user_functions = []
    for block in all_expected_functions:
        current_block_length = len(block)
        user_functions_block = []
        for _ in range(current_block_length):
            if current_index >= len(all_user_functions):
                return formatted_user_functions
            user_functions_block.append(all_user_functions[current_index])
            current_index += 1
        formatted_user_functions.append(user_functions_block)
    for index in range(current_index, len(all_user_functions)):
        formatted_user_functions.append([all_user_functions[index]])
    return formatted_user_functions
