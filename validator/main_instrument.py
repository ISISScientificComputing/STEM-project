import time


class MainInstrument(object):
    x = 1
    y = 1
    z = 1

    def __init__(self, beam_x=1, beam_y=1, beam_z=1):
        self.x = beam_x
        self.y = beam_y
        self.z = beam_z

    def set_position(self, beam_x, beam_y, beam_z):
        positions = [beam_x, beam_y, beam_z]
        for item in positions:
            try:
                int(item)
            except ValueError:
                raise ValueError("Not a number")
            if item not in range(-5, 6):
                raise ValueError("Not in range")

        self.x = beam_x
        self.y = beam_y
        self.z = beam_z

    @staticmethod
    def collect(sleep_timer):
        try:
            int(sleep_timer)
        except ValueError:
            raise ValueError("Not a number")
        time.sleep(sleep_timer)
