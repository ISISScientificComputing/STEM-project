class Validator(object):
    expected_functions = []
    user_functions = []
    different_functions = []
    points = 0
    total = 0
    right_percentage = 0

    def __init__(self, input_list):
        self.expected_functions = input_list

    def execute_user_input(self):
        from validator.user_script import IC
        self.user_functions = IC.track_function
        if len(self.user_functions) == 0:
            print("User Script is empty")
            exit()
        else:
            print("it worked")
        #print(IC.track_function)

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
                    print("Hello World")
            self.right_percentage = self.points/self.total
        print("Percentage of right code: {}%".format(self.right_percentage*100))



