import unittest
from validator.instrument_controls import InstrumentControls
from validator.instrument import Instrument
from validator.sample import Sample


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


class TestInstrument(unittest.TestCase):

    def test_value_is_same_as_input(self):
        main_instrument = MainInstrument()
        main_instrument.set_position(3, 4, -3)
        self.assertEqual(main_instrument.x, 3)
        self.assertEqual(main_instrument.y, 4)
        self.assertEqual(main_instrument.z, -3)

    def test_value_is_not_letter(self):
        main_instrument = MainInstrument()
        self.assertRaises(ValueError, main_instrument.set_position, "Letter", 4, 4)

    def test_set_position_is_within_range(self):
        main_instrument = MainInstrument()
        main_instrument.set_position(5, 5, 5)
        main_instrument.set_position(-5, -5, -5)
        self.assertRaises(ValueError, main_instrument.set_position, -6, -6, -6)
        self.assertRaises(ValueError, main_instrument.set_position, 6, 6, 6)

    def test_wait_is_not_letter(self):
        main_instrument = MainInstrument()
        self.assertRaises(ValueError, main_instrument.set_position, "Letter", 2, 2)


class TestSample(unittest.TestCase):

    def test_value_is_same_as_input_position(self):
        sample = Sample()
        sample.set_position(1, 2, 3)
        self.assertEqual(sample.x, 1)
        self.assertEqual(sample.y, 2)
        self.assertEqual(sample.z, 3)

    def test_value_is_not_letter_position(self):
        sample = Sample()
        self.assertRaises(ValueError, sample.set_position, "Letter", 1, 1)

    def test_set_position_is_within_range(self):
        sample = Sample()
        sample.set_position(5, 5, 5)
        sample.set_position(-5, -5, -5)
        self.assertRaises(ValueError, sample.set_position, -6, -6, -6)
        self.assertRaises(ValueError, sample.set_position, 6, 6, 6)

    def test_set_rotation_is_within_range(self):
        sample = Sample()
        sample.set_rotation(0)
        sample.set_rotation(360)
        self.assertRaises(ValueError, sample.set_rotation, -1)
        self.assertRaises(ValueError, sample.set_rotation, 361)

    def test_value_is_not_letter_rotation(self):
        sample = Sample()
        self.assertRaises(ValueError, sample.set_rotation, "Letter")

    def test_value_is_same_as_input_rotation(self):
        sample = Sample()
        sample.set_rotation(270)
        self.assertEqual(sample.rotation, 270)
