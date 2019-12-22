import csv
import os

from src.main.output_manager import OutputManager
from .calculator import Calculator


class Parser():
    def __init__(self):
        self.output_manager = OutputManager()

    def parse(self, file):
        """Parses the CSV file.

        Checks that the provided path is existing, and that the provided
        file is correct.
        Stores data in memory, escaping the '-' delimiter char that will be
        used by the Calculator class to compute itineraries.
        Instanciates and returns a seeded instance of Calculator class.

        :param file: The path to CSV file.
        :type  file: str

        :return: seeded instance of Calculator class
        :rtype:  src.main.core.calculator.Calculator"""
        if file.startswith('/') is False:
            file = os.path.join(os.getcwd(), file)

        if os.path.exists(file) is False:
            self.output_manager.exit(mode='notfound_csv')

        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            stops = []
            durations = {}
            for row in reader:
                if len(row) != 3 or row[2].isnumeric() is False:
                    self.output_manager.exit(mode='invalid_csv')

                if '-' in list(row[0]):
                    row[0] = row[0].replace('-', '###')

                if '-' in list(row[1]):
                    row[1] = row[1].replace('-', '###')

                row[0] not in stops and stops.append(row[0])
                row[1] not in stops and stops.append(row[1])
                stops_itinerary = sorted([row[0], row[1]])
                durations['{}-{}'.format(
                    stops_itinerary[0], stops_itinerary[1])] = int(row[2])
        return Calculator(stops, durations)
