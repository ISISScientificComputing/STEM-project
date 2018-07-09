import unittest
from stem_project.instrument_controls.instrument import Instrument


class TestInstrument(unittest.TestCase):

    def setUp(self):
        self.instrument = Instrument()

    def test_sample_initialised(self):
        self.assertIsNotNone(self.instrument.new_sample)

    def test_value_is_same_as_input(self):
        self.instrument.set_position(3, 4, -3)
        self.assertEqual(self.instrument.x, 3)
        self.assertEqual(self.instrument.y, 4)
        self.assertEqual(self.instrument.z, -3)

    def test_value_is_not_letter(self):
        self.assertRaises(ValueError, self.instrument.set_position,
                          "Letter", 4, 4)

    def test_set_position_is_within_range(self):
        self.instrument.set_position(5, 5, 5)
        self.instrument.set_position(-5, -5, -5)
        self.assertRaises(ValueError, self.instrument.set_position, -6, -6, -6)
        self.assertRaises(ValueError, self.instrument.set_position, 6, 6, 6)

    def test_wait_is_not_letter(self):
        self.assertRaises(ValueError, self.instrument.set_position,
                          "Letter", 2, 2)
