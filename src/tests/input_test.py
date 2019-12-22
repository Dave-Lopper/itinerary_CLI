
import unittest
from unittest.mock import patch
import sys

from src.main.input_manager import InputManager
from src.main.core.calculator import Calculator
from src.main.core.parser import Parser


def exit(mode=None):
    sys.exit()


def return_values(a, b):
    return 1, 2, 3, 4, 5, 6


class TestInput(unittest.TestCase):
    def setUp(self):
        self.input_manager = InputManager()

    @patch('builtins.input')
    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_input_unexisting_station(self, mock_exit, mock_input):
        calculator = Calculator(['A', 'B', 'C'], {'A-B': 2, 'B-C': 2})
        self.input_manager.calculator = calculator
        mock_input.return_value = 'D'
        with self.assertRaises(SystemExit):
            self.input_manager.input_processing()
        mock_exit.assert_called_with(mode='unexisting_station')

    @patch('builtins.input')
    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_input_invalid_itinerary(self, mock_exit, mock_input):
        calculator = Calculator(['A', 'B', 'C'], {'A-B': 2, 'B-C': 2})
        self.input_manager.calculator = calculator
        mock_input.side_effect = ['A', 'A']
        with self.assertRaises(SystemExit):
            self.input_manager.input_processing()
        mock_exit.assert_called_with(mode='invalid_itinerary')

    @patch('builtins.input')
    @patch('src.main.input_manager.InputManager.calculate',
           side_effect=return_values)
    @patch('src.main.output_manager.OutputManager.itinerary')
    def test_CLI_behaviour_itinerary_output_handling(self, mock_output,
                                                     mock_calculate,
                                                     mock_input):
        mock_input.side_effect = ['A', 'B']
        calculator = Parser().parse('sample.csv')
        self.input_manager.calculator = calculator
        self.input_manager.input_processing()
        mock_calculate.assert_called_with('A', 'B')
        mock_output.assert_called()


if __name__ == '__main__':
    unittest.main()
