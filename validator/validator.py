class Validator(object):
    expected_functions = []
    user_functions = []

    def __init__(self, input_list):
        self.expected_functions = input_list

    def execute_user_input(self):
        from validator.user_script import IC
        print(IC.track_function)
        self.user_functions = IC.track_function
