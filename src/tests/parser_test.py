import unittest

from src.main.core.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser_stops(self):
        parser = Parser()
        calcultor = parser.parse('src/tests/assets/sample_1.csv')
        self.assertEqual(calcultor.stops,
                         ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z'])

    def test_parser_durations(self):
        parser = Parser()
        calcultor = parser.parse('src/tests/assets/sample_2.csv')
        self.assertEqual(calcultor.durations,
                         {'A-B': 10, 'B-C': 5, 'C-D': 7, 'C-E': 8, 'C-F': 6,
                          'F-G': 12, 'G-H': 4, 'G-I': 5, 'I-J': 7})


if __name__ == '__main__':
    unittest.main()
