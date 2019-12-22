
import unittest
from unittest.mock import patch
import sys

from src.main.core.calculator import Calculator
from src.main.core.itinerary import Itinerary


def exit(mode=None):
    sys.exit()


class TestItinerary(unittest.TestCase):
    @patch('builtins.input')
    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_itinerary_unexisting_station(self, mock_exit, mock_input):
        calculator = Calculator(['A', 'B', 'C'], {'A-B': 2, 'B-C': 2})
        itinerary = Itinerary(calculator)
        mock_input.return_value = 'D'
        with self.assertRaises(SystemExit):
            itinerary.process()
        mock_exit.assert_called_with(mode='unexisting_station')

    @patch('builtins.input')
    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_itinerary_invalid_itinerary(self, mock_exit, mock_input):
        calculator = Calculator(['A', 'B', 'C'], {'A-B': 2, 'B-C': 2})
        itinerary = Itinerary(calculator)
        mock_input.side_effect = ['A', 'A']
        with self.assertRaises(SystemExit):
            itinerary.process()
        mock_exit.assert_called_with(mode='invalid_itinerary')


if __name__ == '__main__':
    unittest.main()
