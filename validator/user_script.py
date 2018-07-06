from validator.instrument_controls import InstrumentControls

IC = InstrumentControls()

# Align beam and sample
beam_position = IC.get_beam_position()
IC.set_sample_position(beam_position[0], beam_position[1], beam_position[2])

# set rotation to 0
rotation = 0
IC.set_rotation(0)

# collect 0 seconds of data at 0,120,240 and 360 degrees

while rotation < 360:
    IC.collect_data(0)
    rotation = rotation + 120
    IC.set_rotation(rotation)



