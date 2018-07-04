from validator.instrument_controls import InstrumentControls

IC = InstrumentControls()

# Align beam and sample
beam_position = IC.get_beam_position()
IC.set_sample_position(beam_position[0], beam_position[1], beam_position[2])

# set rotation to 0
rotation = 0
IC.set_rotation(0)

# collect data and rotate
while rotation <= 360:
    IC.collect_data(2)
    rotation = rotation + 120
    IC.set_rotation(rotation)
