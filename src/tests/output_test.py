import unittest
from unittest.mock import patch

from src.main.output_manager import OutputManager


def mock(arg):
    pass


class TestOutput(unittest.TestCase):
    @patch('sys.exit', side_effect=mock)
    def test_output_unescapes_delimiter_char(self, mock_exit):
        tuple_1 = (True, 'Portsmouth###hampton', 'Southwest###London', 0, 4, None)
        output_manager = OutputManager()
        output_manager.itinerary(tuple_1[0], tuple_1[1], tuple_1[2],
                                 tuple_1[3], tuple_1[4], tuple_1[5])
        output_1 = 'Your trip from Portsmouth-hampton to Southwest-London includes 0 stop(s) and will take 4 minutes'
        mock_exit.assert_called_with(output_1)


if __name__ == '__main__':
    unittest.main()
