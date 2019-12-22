from src.main.output_manager import OutputManager


class Itinerary():

    def __init__(self, calculator):
        self.calculator = calculator
        self.output_manager = OutputManager()

    def calculate(self, first_stop, sec_stop):
        return self.calculator.calculate(first_stop, sec_stop)

    def process(self):
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
