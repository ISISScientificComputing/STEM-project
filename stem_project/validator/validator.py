class Validator(object):

    def __init__(self, input_list):
        self.expected_functions = input_list
        self.hints_functions = []
        self.user_functions = []
        self.points = 0
        self.total = 0
        self.right_percentage = 0

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
                if self.expected_functions[index] == self.user_functions[index]:
                    # If the functions are the same
                    self.points = self.points + 10
                else:
                    # If the functions are different
                    self.incorrect_function(self.expected_functions[index][0],
                                            self.user_functions[index][0])
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
                                        self.expected_functions[current_index][0])
        else:
            self.hints_functions.append("You have too many of this function: %s " %
                                        self.user_functions[current_index][0])
