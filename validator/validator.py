from validator.instrument_controls import InstrumentControls


class Validator(object):
    expected_functions = []

    def __init__(self, input_list):
        self.expected_functions = input_list

