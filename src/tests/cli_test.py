
import unittest
from unittest.mock import patch
import sys


def exit(mode=None):
    sys.exit()


class TestCLI(unittest.TestCase):
    @patch('src.main.input_manager.InputManager.command_checking')
    @patch('src.main.input_manager.InputManager.input_processing')
    @patch('src.main.core.parser.Parser.parse')
    def test_CLI_behaviour_itinerary_input_handling(self, mock_parse,
                                                    mock_input_check,
                                                    mock_command_check):
        testargs = ["main.py", "--file=sample.csv"]
        with patch.object(sys, 'argv', testargs):
            import main
            main.Main()
            mock_command_check.assert_called()
            mock_parse.assert_called()
            mock_input_check.assert_called()

    @patch('src.main.output_manager.OutputManager.help', side_effect=exit)
    def test_CLI_behaviour_help(self, mock_help):
        testargs = ["main.py", "--help"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_help.assert_called()

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_CLI_bad_params_handling_invalid_command(self, mock_exit):
        testargs = ["main.py", "invalidcommand"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_exit.assert_called_with(mode='invalid_command')

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_CLI_bad_params_handling_uknown_command(self, mock_exit):
        testargs = ["main.py", "--invalidcommand"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_exit.assert_called_with(mode='uknown_command')

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_CLI_bad_params_handling_unauthorized_extension(self, mock_exit):
        testargs = ["main.py", "--file=sample.txt"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_exit.assert_called_with(mode='unauthorized_extension')

    @patch('src.main.output_manager.OutputManager.exit', side_effect=exit)
    def test_CLI_bad_params_handling_no_csv(self, mock_exit):
        testargs = ["main.py"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                import main
                main.Main()
            mock_exit.assert_called_with(mode='nocsv')


if __name__ == '__main__':
    unittest.main()
