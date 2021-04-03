import unittest

from lmt8x import lmt84_v2t, lmt85_v2t, lmt86_v2t, lmt87_v2t


class LMT84TestCase(unittest.TestCase):

    def test_exact_temp(self):
        self.assertEqual(lmt84_v2t(1299), -50)
        self.assertEqual(lmt84_v2t(1294), -49)
        self.assertEqual(lmt84_v2t(1034), 0)
        self.assertEqual(lmt84_v2t(183), 150)

    def test_linear_interpolation(self):
        self.assertGreater(lmt84_v2t(1298), -50)
        self.assertLess(lmt84_v2t(1298), -49)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            lmt84_v2t(1500)

        with self.assertRaises(ValueError):
            lmt84_v2t(0)


class LMT85TestCase(unittest.TestCase):

    def test_exact_temp(self):
        self.assertEqual(lmt85_v2t(1955), -50)
        self.assertEqual(lmt85_v2t(1949), -49)
        self.assertEqual(lmt85_v2t(1567), 0)
        self.assertEqual(lmt85_v2t(301), 150)

    def test_linear_interpolation(self):
        self.assertGreater(lmt85_v2t(1954), -50)
        self.assertLess(lmt85_v2t(1954), -49)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            lmt85_v2t(2000)

        with self.assertRaises(ValueError):
            lmt85_v2t(0)


class LMT86TestCase(unittest.TestCase):

    def test_exact_temp(self):
        self.assertEqual(lmt86_v2t(2616), -50)
        self.assertEqual(lmt86_v2t(2607), -49)
        self.assertEqual(lmt86_v2t(2100), 0)
        self.assertEqual(lmt86_v2t(420), 150)

    def test_linear_interpolation(self):
        self.assertGreater(lmt86_v2t(2615), -50)
        self.assertLess(lmt86_v2t(2615), -49)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            lmt86_v2t(3000)

        with self.assertRaises(ValueError):
            lmt86_v2t(0)


class LMT87TestCase(unittest.TestCase):

    def test_exact_temp(self):
        self.assertEqual(lmt87_v2t(3277), -50)
        self.assertEqual(lmt87_v2t(3266), -49)
        self.assertEqual(lmt87_v2t(2633), 0)
        self.assertEqual(lmt87_v2t(538), 150)

    def test_linear_interpolation(self):
        self.assertGreater(lmt87_v2t(3276), -50)
        self.assertLess(lmt87_v2t(3276), -49)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            lmt87_v2t(4000)

        with self.assertRaises(ValueError):
            lmt87_v2t(0)
