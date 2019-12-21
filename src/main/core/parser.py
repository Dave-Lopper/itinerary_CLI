import csv
import os
import sys

from .calculator import Calculator


class Parser():
    def parse(self, file):
        if file.startswith('/') is False:
            file = os.path.join(os.getcwd(), file)

        os.path.exists(file) is False and \
            sys.exit('CSV file not found, please check the path')

        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            stops = []
            durations = {}
            for row in reader:
                if len(row) != 3 or row[2].isnumeric() is False:
                    sys.exit('Invalid file provided, please check the format')

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
