import sys

from src.main.core import Parser
from src.main import InputManager


class Main():
    def __init__(self):
        self.input_manager = InputManager()
        value = self.input_manager.command_checking(sys.argv)
        self.input_manager.calculator = Parser().parse(value)
        self.input_manager.input_processing()


if __name__ == '__main__':
    Main()
