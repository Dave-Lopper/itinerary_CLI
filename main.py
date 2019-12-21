import sys

from src.main.core import Parser, Itinerary
from src.main import InputManager


class Main():
    def __init__(self):
        self.input_manager = InputManager()
        value = self.input_manager.input_checking(sys.argv)
        calculator = Parser().parse(value)
        self.itinerary_manager = Itinerary(calculator)
        self.itinerary_manager.process()


if __name__ == '__main__':
    Main()
