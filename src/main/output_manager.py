import sys


class OutputManager():
    def itinerary(self, success, departure, arrival,
                  stops, duration, alternative_arrival=None):

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
