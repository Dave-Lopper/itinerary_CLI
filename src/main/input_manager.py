import sys

from .output_manager import OutputManager
from src.tests import TestManager


class InputManager():
    def __init__(self):
        self.output_manager = OutputManager()
        self.test_manager = TestManager()

    def input_checking(self, args):
        if len(args) == 1:
            sys.exit(
                'Please provide the CSV file, try using the --help argument')

        argument = args[1]
        if argument.startswith('-') is False:
            sys.exit('Invalid command format, try using the --help argument')

        command = list(filter(lambda x: x != '', argument.split('-')))[0]
        if len(command.split('=')) == 1 and command not in ['help', 'test']:
            sys.exit('Invalid command format, try using the --help argument')

        command == 'help' and self.output_manager.help()
        if command == 'test':
            self.test_manager.test()
            sys.exit()

        command, argument = command.split('=')
        command != 'file' and sys.exit(
            'Invalid command, try using the --help argument')

        argument.endswith('.csv') is False and \
            sys.exit('Invalid file provided (.csv only), try using the --help argument')

        return argument
