import unittest
from instrumentclass import InstrumentControls


class TestInstrumentControls(unittest.TestCase):

    def test_print_value_with_numbers(self):
        instrument_controls = InstrumentControls()
        instrument_controls.print_value(3)

    def test_print_value_with_letters(self):
        instrument_controls = InstrumentControls()
        instrument_controls.print_value("Hello")

    def test_add_with_numbers(self):
        instrument_controls = InstrumentControls()
        actual = instrument_controls.add(3, 5)
        expected = 8
        self.assertEqual(actual, expected)

    def test_add_with_letters(self):
        instrument_controls = InstrumentControls()
        self.assertRaises(ValueError, instrument_controls.add, 'letter', 'letter')

    def test_wait_with_letters(self):
        instrument_controls = InstrumentControls()
        self.assertRaises(ValueError, instrument_controls.wait, "Letter")





