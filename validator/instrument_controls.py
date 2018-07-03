import time
from validator.instrument import Instrument


class InstrumentControls(object):
    new_instrument = None
    print_counter = 0
    add_counter = 0
    wait_counter = 0

    def __init__(self):
        self.new_instrument = Instrument()
        self.print_counter = 0
        self.add_counter = 0
        self.wait_counter = 0

    def print_value(self, value_to_print):
        print(value_to_print)
        self.print_counter = self.print_counter + 1

    def add(self, first, second):
        try:
            int(first)
            int(second)
        except ValueError:
            raise ValueError("Not a number")
        self.add_counter = self.add_counter + 1
        ans = first + second
        return ans

    def wait(self, sleep_timer):
        try:
            int(sleep_timer)
        except ValueError:
            raise ValueError("Not a number")
        time.sleep(sleep_timer)
        self.wait_counter = self.wait_counter + 1
