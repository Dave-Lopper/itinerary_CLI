
import unittest
from unittest.mock import patch
import sys

from src.main.core.itinerary import Itinerary
from src.main.core.parser import Parser


def return_values(a, b):
    return 1, 2, 3, 4, 5, 6


def exit():
    sys.exit()


class TestCLI(unittest.TestCase):
    @patch('src.main.input_manager.InputManager.input_checking')
    @patch('src.main.core.parser.Parser.parse')
    @patch('src.main.core.itinerary.Itinerary.process')
    def test_CLI_behaviour_itinerary_input_handling(self, mock_process,
                                                    mock_parse,
                                                    mock_input_check):
        testargs = ["main.py", "--file=sample.csv"]
        with patch.object(sys, 'argv', testargs):
            import main
            main.Main()
            mock_input_check.assert_called()
            mock_parse.assert_called()
            mock_process.assert_called()

    @patch('builtins.input')
    @patch('src.main.core.itinerary.Itinerary.calculate',
           side_effect=return_values)
    @patch('src.main.output_manager.OutputManager.itinerary')
    def test_CLI_behaviour_itinerary_output_handling(self, mock_output,
                                                     mock_calculate,
                                                     mock_input):
        mock_input.side_effect = ['A', 'B']
        calculator = Parser().parse('sample.csv')
        itinerary_manager = Itinerary(calculator)
        itinerary_manager.process()
        mock_calculate.assert_called_with('A', 'B')
        mock_output.assert_called()

    @patch('src.main.output_manager.OutputManager.help', side_effect=exit)
    def test_CLI_behaviour_help(self, mock_help):
        testargs = ["main.py", "--help"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_help.assert_called()


if __name__ == '__main__':
    unittest.main()
