import sys
import unittest
from unittest.mock import patch

from src.main.core.parser import Parser


def exit(mode=None):
    sys.exit()


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parser_stops(self):
        calcultor = self.parser.parse('src/tests/assets/sample_1.csv')
        self.assertEqual(calcultor.stops,
                         ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z'])

    def test_parser_durations(self):
        calcultor = self.parser.parse('src/tests/assets/sample_2.csv')
        self.assertEqual(calcultor.durations,
                         {'A-B': 10, 'B-C': 5, 'C-D': 7, 'C-E': 8, 'C-F': 6,
                          'F-G': 12, 'G-H': 4, 'G-I': 5, 'I-J': 7})

    def test_parser_escape_delimiter_char(self):
        calcultor = self.parser.parse('src/tests/assets/sample_3.csv')
        self.assertEqual(calcultor.stops,
                         ['Portsmouth###hampton', 'Southwest###London',
                          'Great###Portland###Street', 'Baker###Street'])
        self.assertEqual(calcultor.durations,
                         {'Portsmouth###hampton-Southwest###London': 1,
                          'Baker###Street-Great###Portland###Street': 3,
                          'Baker###Street-Southwest###London': 4})

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_parser_notfound_csv(self, mock_exit):
        with self.assertRaises(SystemExit):
            self.parser.parse('unexisting/path/to/unexisting/file.csv')
        mock_exit.assert_called_with(mode='notfound_csv')

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_parser_invalid_csv(self, mock_exit):
        with self.assertRaises(SystemExit):
            self.parser.parse('src/tests/assets/sample_invalid.csv')
        mock_exit.assert_called_with(mode='invalid_csv')


if __name__ == '__main__':
    unittest.main()
