from stem_project.validator.function_wrapper import FunctionWrapper


class FunctionBlock(object):

    function_wrappers = None

    def __init__(self, list_of_function_wrappers):
        for function_wrapper in list_of_function_wrappers:
            try:
                isinstance(function_wrapper, FunctionWrapper)
            except Exception:
                raise Exception("This is not a function wrapper")
            self.function_wrappers = list_of_function_wrappers

    def __eq__(self, other):
        self.function_wrappers.sort()
        other.function_wrappers.sort()
        for index in range(len(self.function_wrappers)):
            if self.function_wrappers[index] == other.function_wrappers[index]:
                return True
        return False
