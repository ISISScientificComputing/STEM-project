class Validator(object):
    expected_functions = []
    user_functions = []
    hints_functions = []
    points = 0
    total = 0
    right_percentage = 0

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

        # Identify short list

        max_iterations = len(self.expected_functions)
        min_iterations = len(self.user_functions)

        if len(self.user_functions) > len(self.expected_functions):
            max_iterations = len(self.user_functions)
            min_iterations = len(self.expected_functions)

        self.total = max_iterations*10

        for index in range(max_iterations):
            if index < min_iterations:
                if self.expected_functions[index] == self.user_functions[index]:
                    self.points = self.points + 10
                else:
                    if "set_sample_position" == self.user_functions[index][0]:
                        self.hints_functions.append("Your sample positions is not quite right")
                    elif "collect_data" == self.user_functions[index][0]:
                        self.hints_functions.append("Your wait time is not quite right")
                    elif "set_sample_rotation" == self.user_functions[index][0]:
                        self.hints_functions.append("Your sample rotation is not quite right")
            else:
                if max_iterations == len(self.expected_functions):
                    self.hints_functions.append("You are missing this function: " + self.expected_functions[index][0])
                else:
                    self.hints_functions.append("You have too many of this function: " + self.user_functions[index][0])
        self.right_percentage = (self.points/self.total)*100
