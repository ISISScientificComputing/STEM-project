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
