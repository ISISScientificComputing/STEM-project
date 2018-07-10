from stem_project.instrument_controls.instrument import Instrument


class InstrumentControls(object):

    def __init__(self):
        self.new_instrument = Instrument()
        self.track_function = []

    def set_sample_rotation(self, rotation):
        self.new_instrument.new_sample.set_rotation(rotation)
        self.track_function.append(("set_sample_rotation", [rotation]))

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
