import sys

from src.main.output_manager import OutputManager


class Itinerary():

    def __init__(self, calculator):
        self.calculator = calculator
        self.output_manager = OutputManager()

    def calculate(self, first_stop, sec_stop):
        return self.calculator.calculate(first_stop, sec_stop)

    def process(self):
        first_stop = input('Please enter your departure station : \n')
        first_stop not in self.calculator.stops and sys.exit(
            'Provided station missing from data source')

        sec_stop = input('Please enter your arrival station : \n')
        sec_stop not in self.calculator.stops and sys.exit(
            'Provided station missing from data source')
        sec_stop == first_stop and sys.exit(
            'Arrival and departure stations are the same')
        success, first_stop, last_stop, nb_stops, time, alt_arrival = \
            self.calculate(first_stop, sec_stop)

        self.output_manager.itinerary(success, first_stop, last_stop, nb_stops,
                                      time, alt_arrival)
