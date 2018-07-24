from stem_project.validator.function_wrapper import FunctionWrapper


class FunctionBlock(object):

    function_wrappers = None

    def __init__(self, list_of_function_wrappers):
        self.efficient_function_wrappers = []
        for function_wrapper in list_of_function_wrappers:
            try:
                isinstance(function_wrapper, FunctionWrapper)
            except Exception:
                raise Exception("This is not a function wrapper")
            self.function_wrappers = list_of_function_wrappers
        self.evaluate_same_functions()

    def __eq__(self, other):
        self.function_wrappers.sort()
        other.function_wrappers.sort()
        for index in range(len(self.function_wrappers)):
            if self.function_wrappers[index] == other.function_wrappers[index]:
                return True
        return False

    def split_block_into_sublists(self):
        self.function_wrappers.sort()
        functions_dictionary = {self.function_wrappers[0].name_of_function:[self.function_wrappers[0]]}
        for current in self.function_wrappers[1:]:
            if current.name_of_function in functions_dictionary.keys():
                functions_dictionary[current.name_of_function].append(current)
            else:
                functions_dictionary[current.name_of_function] = [current]
        return functions_dictionary

    def evaluate_same_functions(self):
        functions_dictionary = self.split_block_into_sublists()
        for key in functions_dictionary.keys():
            all_function_wrappers = functions_dictionary[key]
            args = all_function_wrappers[0].list_of_arguments
            for function_wrapper in all_function_wrappers[1:]:
                args += function_wrapper.list_of_arguments
            self.efficient_function_wrappers.append(FunctionWrapper(key, args))
