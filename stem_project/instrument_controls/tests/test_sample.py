import unittest
from stem_project.instrument_controls.sample import Sample


class TestSample(unittest.TestCase):

    def setUp(self):
        self.sample = Sample()

    def test_value_is_same_as_input_position(self):
        self.sample.set_position(1, 2, 3)
        self.assertEqual(self.sample.x, 1)
        self.assertEqual(self.sample.y, 2)
        self.assertEqual(self.sample.z, 3)

    def test_value_is_not_letter_position(self):
        self.assertRaises(ValueError, self.sample.set_position,
                          "Letter", 1, 1)

    def test_set_position_is_within_range(self):
        self.sample.set_position(5, 5, 5)
        self.sample.set_position(-5, -5, -5)
        self.assertRaises(ValueError, self.sample.set_position, -6, -6, -6)
        self.assertRaises(ValueError, self.sample.set_position, 6, 6, 6)

    def test_set_rotation_is_within_range(self):
        self.sample.set_rotation(0)
        self.sample.set_rotation(360)
        self.assertRaises(ValueError, self.sample.set_rotation, -1)
        self.assertRaises(ValueError, self.sample.set_rotation, 361)

    def test_value_is_not_letter_rotation(self):
        self.assertRaises(ValueError, self.sample.set_rotation, "Letter")

    def test_value_is_same_as_input_rotation(self):
        self.sample.set_rotation(270)
        self.assertEqual(self.sample.rotation, 270)
