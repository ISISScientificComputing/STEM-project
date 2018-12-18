class FunctionWrapper (object):
    name_of_function = None
    list_of_arguments = None

    def __init__(self, name, arguments):
        try:
            self.name_of_function = str(name)
        except ValueError:
            raise ValueError("Not a string")
        self.list_of_arguments = arguments

    def __gt__(self, other):
        if self.name_of_function > other.name_of_function:
            return self
        if self.name_of_function == other.name_of_function:
            if len(self.list_of_arguments) > len(other.list_of_arguments):
                return self
        if self.name_of_function == other.name_of_function:
            if len(self.list_of_arguments) == len(other.list_of_arguments):
                if self.list_of_arguments > other.list_of_arguments:
                    return self

    def __eq__(self, other):
        if isinstance(other, FunctionWrapper):
            if self.name_of_function == other.name_of_function:
                if self.list_of_arguments == other.list_of_arguments:
                    return True
        return False
