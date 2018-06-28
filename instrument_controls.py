import time


class InstrumentControls(object):

    def print_value(self, value_to_print):
        print(value_to_print)

    def add(self, first, second):
        try:
            int(first)
            int(second)
        except ValueError:
            raise ValueError("Not a number")
        ans = first + second
        return ans

    def wait(self, sleeptimer):
        try:
            int(sleeptimer)
        except ValueError:
            raise ValueError("Not a number")
        time.sleep(sleeptimer)

