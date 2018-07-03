import time
from validator.instrument import Instrument


class InstrumentControls(object):
    new_instrument = None
    track_function = []

    def __init__(self):
        self.new_instrument = Instrument()
        self.track_function = []

    def print_value(self, value_to_print):
        print(value_to_print)
        self.track_function.append("print_value")

    def add(self, first, second):
        try:
            int(first)
            int(second)
        except ValueError:
            raise ValueError("Not a number")
        self.track_function.append("add")
        ans = first + second
        return ans

    def wait(self, sleep_timer):
        try:
            int(sleep_timer)
        except ValueError:
            raise ValueError("Not a number")
        time.sleep(sleep_timer)
        self.track_function.append("wait")
