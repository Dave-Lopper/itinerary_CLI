import unittest

from src.main.core.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                                     {'B-C': 5, 'B-D': 7, 'D-E': 3, 'E-F': 3,
                                     'E-G': 5})

    def test_calculator_direct_itinerary(self):
        output_bc = (True, 'B', 'C', 0, 5, None)
        self.assertEqual(self.calculator.calculate('B', 'C'), output_bc)

        output_bd = (True, 'B', 'D', 0, 7, None)
        self.assertEqual(self.calculator.calculate('B', 'D'), output_bd)

    def test_calculator_direct_itinerary_reversed(self):
        output_cb = (True, 'C', 'B', 0, 5, None)
        self.assertEqual(self.calculator.calculate('C', 'B'), output_cb)

        output_db = (True, 'D', 'B', 0, 7, None)
        self.assertEqual(self.calculator.calculate('D', 'B'), output_db)

    def test_calculator_complex_itinerary(self):
        output_bf = (True, 'B', 'F', 2, 13, None)
        self.assertEqual(self.calculator.calculate('B', 'F'), output_bf)

        output_be = (True, 'B', 'E', 1, 10, None)
        self.assertEqual(self.calculator.calculate('B', 'E'), output_be)

    def test_calculator_complex_itinerary_reversed(self):
        output_fb = (True, 'F', 'B', 2, 13, None)
        self.assertEqual(self.calculator.calculate('F', 'B'), output_fb)

        output_eb = (True, 'E', 'B', 1, 10, None)
        self.assertEqual(self.calculator.calculate('E', 'B'), output_eb)

    def test_calculator_unexisting_ride(self):
        output_cd = (False, 'C', 'D', 0, 0, None)
        self.assertEqual(self.calculator.calculate('C', 'D'), output_cd)

        output_fg = (False, 'F', 'G', 0, 0, None)
        self.assertEqual(self.calculator.calculate('F', 'G'), output_fg)

    def test_calculator_unexisting_ride_reversed(self):
        output_dc = (False, 'D', 'C', 0, 0, None)
        self.assertEqual(self.calculator.calculate('D', 'C'), output_dc)

        output_gf = (False, 'G', 'F', 0, 0, None)
        self.assertEqual(self.calculator.calculate('G', 'F'), output_gf)

    def test_calculator_unexisting_itinerary(self):
        output_bh = (False, 'B', 'H', 2, 15, 'G')
        self.assertEqual(self.calculator.calculate('B', 'H'), output_bh)

        output_dh = (False, 'D', 'H', 1, 8, 'G')
        self.assertEqual(self.calculator.calculate('D', 'H'), output_dh)

    def test_calculator_unexisting_itinerary_reversed(self):
        output_ga = (False, 'G', 'A', 2, 15, 'B')
        self.assertEqual(self.calculator.calculate('G', 'A'), output_ga)

        output_fa = (False, 'F', 'A', 2, 13, 'B')
        self.assertEqual(self.calculator.calculate('F', 'A'), output_fa)


if __name__ == '__main__':
    unittest.main()
