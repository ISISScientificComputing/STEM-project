from validator.instrument import Instrument


class InstrumentControls(object):
    new_instrument = None
    track_function = []

    def __init__(self):
        self.new_instrument = Instrument()
        self.track_function = []

    def print_value(self, value_to_print):
        print(value_to_print)
        self.track_function.append(("print_value", [value_to_print]))

    def add(self, first, second):
        try:
            int(first)
            int(second)
        except ValueError:
            raise ValueError("Not a number")
        self.track_function.append(("add", [first, second]))
        ans = first + second
        return ans

    def set_rotation(self, rotation):
        self.new_instrument.new_sample.set_rotation(rotation)
        self.track_function.append(("set_rotation", [rotation]))

    def get_rotation(self):
        return self.new_instrument.new_sample.rotation

    def set_beam_position(self, x, y, z):
        self.new_instrument.set_position(x, y, z)
        self.track_function.append(("set_beam_position", [x, y, z]))

    def get_beam_position(self):
        return self.new_instrument.x, self.new_instrument.y, self.new_instrument.z

    def set_sample_position(self, x, y, z):
        self.new_instrument.new_sample.set_position(x, y, z)
        self.track_function.append(("set_sample_position", [x, y, z]))

    def get_sample_position(self):
        return self.new_instrument.new_sample.x, self.new_instrument.new_sample.y, self.new_instrument.new_sample.z

    def collect_data(self, sleep_timer):
        self.new_instrument.collect(sleep_timer)
        self.track_function.append(("collect_data", [sleep_timer]))
