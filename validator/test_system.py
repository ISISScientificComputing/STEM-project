import unittest

from validator.instrument_controls import InstrumentControls
from validator.instrument import Instrument


class TestInstanceCreated(unittest.TestCase):

    def test_instrument_no_longer_none(self):
        instrument_controls = InstrumentControls()
        self.assertIsNotNone(instrument_controls.new_instrument)

    def test_sample_no_longer_none(self):
        new_instrument = Instrument()
        self.assertIsNotNone(new_instrument.new_sample)

    def test_list_is_correct(self):
        instrument_controls = InstrumentControls()
        expected_result = ["print_value", "add", "wait"]
        instrument_controls.print_value("")
        instrument_controls.add(1, 1)
        instrument_controls.wait(0)
        self.assertListEqual(instrument_controls.track_function, expected_result)

    def test_function_is_called(self):
        instrument_controls = InstrumentControls()
        instrument_controls.print_value("")
        instrument_controls.print_value("")
        instrument_controls.print_value("")
        self.assertEqual(instrument_controls.track_function.count("print_value"), 3)

    def test_add_list_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.add(1, 2)
        instrument_controls.add(3, 4)
        instrument_controls.add(5, 6)
        self.assertEqual(instrument_controls.track_function.count("add"), 3)

    def test_wait_list_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.wait(0)
        instrument_controls.wait(0)
        instrument_controls.wait(0)
        self.assertEqual(instrument_controls.track_function.count("wait"), 3)
