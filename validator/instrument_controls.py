import time


class InstrumentControls(object):

    @staticmethod
    def print_value(value_to_print):
        print(value_to_print)

    @staticmethod
    def add(first, second):
        try:
            int(first)
            int(second)
        except ValueError:
            raise ValueError("Not a number")
        ans = first + second
        return ans

    @staticmethod
    def wait(sleep_timer):
        try:
            int(sleep_timer)
        except ValueError:
            raise ValueError("Not a number")
        time.sleep(sleep_timer)


