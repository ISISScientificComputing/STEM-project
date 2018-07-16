import unittest
from stem_project.instrument_controls.instrument_controls import InstrumentControls
from stem_project.validator.function_wrapper import FunctionWrapper
from stem_project.validator.validator import compare_function_wrappers

class TestInstrumentControls(unittest.TestCase):

    def setUp(self):
        self.instrument_controls = InstrumentControls()

    def test_instrument_no_longer_none(self):
        self.assertIsNotNone(self.instrument_controls.new_instrument)

    def test_set_rotation(self):
        self.instrument_controls.set_sample_rotation(270)
        self.assertEqual(self.instrument_controls.new_instrument.new_sample.rotation, 270)
        self.assertEqual(self.instrument_controls.get_rotation(), 270)

    def test_set_sample_position(self):
        self.instrument_controls.set_sample_position(1, 2, 3)
        self.assertEqual(self.instrument_controls.new_instrument.new_sample.x, 1)
        self.assertEqual(self.instrument_controls.new_instrument.new_sample.y, 2)
        self.assertEqual(self.instrument_controls.new_instrument.new_sample.z, 3)
        self.assertEqual(self.instrument_controls.get_sample_position(), (1, 2, 3))

    def test_set_beam_position(self):
        self.instrument_controls.set_beam_position(1, 2, 3)
        self.assertEqual(self.instrument_controls.new_instrument.x, 1)
        self.assertEqual(self.instrument_controls.new_instrument.y, 2)
        self.assertEqual(self.instrument_controls.new_instrument.z, 3)
        self.assertEqual(self.instrument_controls.get_beam_position(), (1, 2, 3))

    def test_track_function_list_correctly_updated(self):
        instrument_controls = InstrumentControls()
        set_sample_rotation_1 = FunctionWrapper("set_sample_rotation", [1])
        set_sample_position_1_1_1 = FunctionWrapper("set_sample_position", [1, 1, 1])
        expected_result = [set_sample_rotation_1, set_sample_position_1_1_1]
        instrument_controls.set_sample_rotation(1)
        instrument_controls.set_sample_position(1, 1, 1)
        self.assertTrue(compare_function_wrappers(instrument_controls.track_function[0], expected_result[0]))
        self.assertTrue(compare_function_wrappers(instrument_controls.track_function[1], expected_result[1]))

    def test_track_function_list_with_multiple_calls(self):
        instrument_controls = InstrumentControls()
        instrument_controls.set_sample_rotation(1)
        instrument_controls.set_sample_rotation(2)
        instrument_controls.set_sample_rotation(3)
        counter = 0
        for function_tuple in instrument_controls.track_function:
            if function_tuple.name_of_function == "set_sample_rotation":
                counter = counter + 1
        self.assertEqual(counter, 3)
