import sys


class OutputManager():
    def itinerary(self, success, departure, arrival,
                  stops, duration, alternative_arrival=None):
        """Gets the output of Calculator.calculate() method,
           prints it into a user readable output and exits.

            :param mode: Determines the output message.
            :type mode:  str

            :param success: Wether or not the function could find an itinerary
                linking the two given points.
            :param first_stop: The starting point of the itinerary
            :param last_stop:  The ending point of the itinerary
            :param nb_stops:   Number of connections to make in the itinerary
            :param duration:   Number of minutes to complete the itinerary
            :param alternative_arrival: Instanciated if success is false,
                and an alternative itinerary could be found, if success
                is false and alternative_arrival is none, there is no route
                between the two given stations.

            :type success:             boolean
            :type first_stop:          str
            :type last_stop:           str
            :type nb_stops:            int
            :type duration:            int
            :type alternative_arrival: str"""

        if departure is not None and '###' in departure:
            departure = departure.replace('###', '-')
        if arrival is not None and '###' in arrival:
            arrival = arrival.replace('###', '-')
        if alternative_arrival is not None and '###' in alternative_arrival:
            alternative_arrival = alternative_arrival.replace('###', '-')

        if success:
            visual_output = \
                "Your trip from {} to {} includes {} stop(s) and will take {} minutes" \
                .format(departure, arrival, stops, duration)
            sys.exit(visual_output)
        else:
            if alternative_arrival is not None:
                visual_output = \
                    "There is no route from {} to {}, the furthest you can go is {}, including {} stops and will take {} minutes" \
                    .format(departure, arrival,
                            alternative_arrival, stops, duration)
                sys.exit(visual_output)
            else:
                visual_output = \
                    "There is no route from {} to {}".format(departure,
                                                             arrival)
                sys.exit(visual_output)

    def exit(self, mode):
        """Exits with custom output message.

            :param mode: Determines the output message.
            :type mode:  str"""

        if mode == 'no_csv':
            sys.exit(
                'Please provide the CSV file, try using the --help command')
        elif mode == 'invalid_command':
            sys.exit(
                'Invalid command format, try using the --help command')
        elif mode == 'uknown_command':
            sys.exit('Uknown command, try using the --help command')
        elif mode == 'unauthorized_extension':
            sys.exit(
                'Invalid file provided (.csv only), try using the --help command')
        elif mode == 'invalid_scv':
            sys.exit('Invalid file provided, please check the format')
        elif mode == 'notfound_csv':
            sys.exit('CSV file not found, please check the path')
        elif mode == 'unexisting_station':
            sys.exit('Provided station missing from data source')
        elif mode == 'invalid_itinerary':
            sys.exit('Arrival and departure stations are the same')

    def help(self):
        visual_output = """
        Hi ! Welcome in the itinerary CLI !
        Here you can obtain the fastest itinerary between two point that you
        will have to provide !

        You will also have to provide a .csv file containing departure,
        arrival point and the duration of the ride between those two points.

        Example of valid .csv :
        Ploen Chit, Sukhumvit, 10
        Sukhumvit, Phetchaburi, 15

        Let's get started ?
        python main.py --file=/path/to/file.csv

        Developer's corner :
        Wanna make sure everything's on tracks ? Try running :
        python main.py --test
        """

        sys.exit(visual_output)
