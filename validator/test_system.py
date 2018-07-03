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
        expected_result = [("print_value", [""]), ("add", [1, 1]), ("wait", [0])]
        instrument_controls.print_value("")
        instrument_controls.add(1, 1)
        instrument_controls.wait(0)
        self.assertListEqual(instrument_controls.track_function, expected_result)

    def test_function_is_called(self):
        instrument_controls = InstrumentControls()
        instrument_controls.print_value("Hello")
        instrument_controls.print_value("World")
        instrument_controls.print_value("Python")
        counter = 0
        for function_tuple in instrument_controls.track_function:
            if function_tuple[0] == "print_value":
                counter = counter + 1
        self.assertEqual(counter, 3)

    def test_add_list_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.add(1, 2)
        instrument_controls.add(3, 4)
        instrument_controls.add(5, 6)
        counter = 0
        for function_tuple in instrument_controls.track_function:
            if function_tuple[0] == "add":
                counter = counter + 1
        self.assertEqual(counter, 3)

    def test_wait_list_works(self):
        instrument_controls = InstrumentControls()
        instrument_controls.wait(0)
        instrument_controls.wait(1)
        instrument_controls.wait(2)
        counter = 0
        for function_tuple in instrument_controls.track_function:
            if function_tuple[0] == "wait":
                counter = counter + 1
        self.assertEqual(counter, 3)
