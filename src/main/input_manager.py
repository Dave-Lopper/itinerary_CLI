import sys

from .output_manager import OutputManager
from src.tests import TestManager


class InputManager():
    calculator = None

    def __init__(self):
        self.output_manager = OutputManager()
        self.test_manager = TestManager()

    def calculate(self, first_stop, last_stop):
        return self.calculator.calculate(first_stop, last_stop)

    def command_checking(self, args):
        """Checks the python command arguments.

        :param args: returned value of sys.argv
        :type  args: list

        :return: path to CSV file
        :rtype:  str"""
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

    def input_processing(self):
        """Processes the user interaction.

        Inputs the starting and ending point of itinerary,
        Checks validity of provided data,
        Calls the calculate() method of the Calculator class
        and pass it to the itinerary() method of OutputManager class."""

        first_stop = input('Please enter your departure station : \n')
        if first_stop not in self.calculator.stops:
            self.output_manager.exit(mode='unexisting_station')

        sec_stop = input('Please enter your arrival station : \n')
        if sec_stop not in self.calculator.stops:
            self.output_manager.exit(mode='unexisting_station')

        if sec_stop == first_stop:
            self.output_manager.exit(mode='invalid_itinerary')

        success, first_stop, last_stop, nb_stops, time, alt_arrival = \
            self.calculate(first_stop, sec_stop)

        self.output_manager.itinerary(success, first_stop, last_stop, nb_stops,
                                      time, alt_arrival)
