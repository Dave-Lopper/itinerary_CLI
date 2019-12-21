import sys


class OutputManager():
    def itinerary(self, success, departure, arrival,
                  stops, duration, alternative_arrival=None):
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
