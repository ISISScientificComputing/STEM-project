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

    def test_function_is_called(self):
        instrument_controls = InstrumentControls()
        instrument_controls.print_value("")
        instrument_controls.print_value("")
        instrument_controls.print_value("")
        self.assertEqual(instrument_controls.print_counter, 3)

    def test_add_counter_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.add(1, 2)
        instrument_controls.add(3, 4)
        instrument_controls.add(5, 6)
        self.assertEqual(instrument_controls.add_counter, 3)

    def test_wait_counter_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.wait(1)
        instrument_controls.wait(2)
        instrument_controls.wait(3)
        self.assertEqual(instrument_controls.wait_counter, 3)
