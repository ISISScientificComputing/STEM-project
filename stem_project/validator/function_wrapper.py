class FunctionWrapper (object):
    name_of_function = None
    list_of_arguments = None

    def __init__(self, name, arguments):
        try:
            self.name_of_function = str(name)
        except ValueError:
            raise ValueError("Not a string")
        self.list_of_arguments = arguments