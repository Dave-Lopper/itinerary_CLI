import sys

from .output_manager import OutputManager
from src.tests import TestManager


class InputManager():
    def __init__(self):
        self.output_manager = OutputManager()
        self.test_manager = TestManager()

    def input_checking(self, args):
        if len(args) == 1:
            self.output_manager.exit(mode='nocsv')

        argument = args[1]
        if argument.startswith('-') is False:
            self.output_manager.exit(mode='invalid_command')

        command = list(filter(lambda x: x != '', argument.split('-')))[0]

        if len(command.split('=')) == 1 and command not in ['help', 'test']:
            self.output_manager.exit(mode='uknown_command')

        command == 'help' and self.output_manager.help()
        if command == 'test':
            self.test_manager.test()
            sys.exit()

        command, argument = command.split('=')
        command != 'file' and self.output_manager.exit(mode='uknown_command')

        argument.endswith('.csv') is False and \
            self.output_manager.exit(mode='unauthorized_extension')

        return argument
