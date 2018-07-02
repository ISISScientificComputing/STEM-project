class Sample(object):
    rotation = 0
    x = 1
    y = 1
    z = 1

    def __init__(self, sample_x=1, sample_y=1, sample_z=1, sample_rotation=0):
        self.x = sample_x
        self.y = sample_y
        self.z = sample_z
        self.rotation = sample_rotation

    def set_position(self, sample_x, sample_y, sample_z):
        positions = [sample_x, sample_y, sample_z]
        for item in positions:
            try:
                int(item)
            except ValueError:
                raise ValueError("Not a number")
            if item not in range(-5, 6):
                raise ValueError("Not in the range")

        self.x = sample_x
        self.y = sample_y
        self.z = sample_z

    def set_rotation(self, sample_rotation):
        self.rotation = sample_rotation
        try:
            int(sample_rotation)
        except ValueError:
            raise ValueError("Not a number")
        if sample_rotation not in range(0, 361):
            raise ValueError("Not in range")