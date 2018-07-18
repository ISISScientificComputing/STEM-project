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
        my_list = []
        for line in f:
            my_list.append(line)
            words = line.split()
            function_name = words[0]
            # remove first item from words list
            words.remove(words[0])
            # Add line that splits up a string where there are commas
            arguements = words[0].split(",")
            # for each item in the list of arguments
                # try to cast the argument to a str
                # except a ValueErrot
                # if we get a value error just leave the argument as it is
                # if we can cast it to an integer make sure we update this in the list
            try:
                words = [int(i) for i in arguements]
            except ValueError:
                pass
            self.expected_functions.append(FunctionWrapper(function_name, words))

        f.close()




    def execute_user_input(self):
        from stem_project.user_script.user_script import IC
        self.user_functions = IC.track_function
        if len(self.user_functions) == 0:
            raise IOError("No user functions found")
        self.validate_functions()

    def validate_functions(self):
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
                if compare_function_wrappers(self.expected_functions[index], self.user_functions[index]):
                    # If the functions are the same
                    self.points = self.points + 10
                else:
                    # If the functions are different
                    self.incorrect_function(self.expected_functions[index].name_of_function,
                                            self.user_functions[index].name_of_function)
            else:
                self.function_list_length_mismatch(index)

        self.right_percentage = (self.points/self.total)*100

    def incorrect_function(self, expected_function_name, actual_function_name):
        if expected_function_name == actual_function_name:
            self.hints_functions.append("%s is the correct function, "
                                        "but does not have the correct parameters." % actual_function_name)
        else:
            self.hints_functions.append("%s is not the correct function." % actual_function_name)

    def function_list_length_mismatch(self, current_index):
        """
        If the expected_function list and the user_functions list are not of equal length
        :param current_index: The current index in the list to check
        """
        if len(self.expected_functions) > len(self.user_functions):
            self.hints_functions.append("You are missing this function: %s" %
                                        self.expected_functions[current_index].name_of_function)
        else:
            self.hints_functions.append("You have too many of this function: %s " %
                                        self.user_functions[current_index].name_of_function)


def compare_function_wrappers(function_wrapper_1, function_wrapper_2):
    if function_wrapper_1.name_of_function == function_wrapper_2.name_of_function:
        if function_wrapper_1.list_of_arguements == function_wrapper_2.list_of_arguements:
            return True
    return False
