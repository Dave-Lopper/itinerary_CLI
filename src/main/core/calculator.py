class Calculator():
    def __init__(self, stops, durations):
        self.stops = stops
        self.durations = durations

    def calculate(self, first_stop, sec_stop):
        journey_length = abs(self.stops.index(
            first_stop) - self.stops.index(sec_stop))
        formatted_journey = sorted([first_stop, sec_stop])
        formatted_string = '{}-{}'.format(formatted_journey[0],
                                          formatted_journey[1])
        direct_itineraries = list(self.durations.keys())
        reversed = False
        if (self.stops.index(first_stop) > self.stops.index(sec_stop)):
            reversed = True

        if journey_length == 1:
            if formatted_string in direct_itineraries:
                nb_stops = 0
                time = self.durations[formatted_string]
                return True, first_stop, sec_stop, 0, time, None
            else:
                return False, first_stop, sec_stop, 0, 0, None

        stop_one = first_stop
        time = 0
        steps = []
        while stop_one != sec_stop:
            index = 1 if reversed is True else 0
            possible_rides = list(filter(
                lambda x: stop_one == x.split('-')[index],
                direct_itineraries
            ))
            formatted_rides = []

            index = 0 if reversed is True else 1
            if len(list(filter(lambda x: x.split('-')[index] == sec_stop,
                               possible_rides))) > 0:
                last_ride = list(filter(
                    lambda x: x.split('-')[index] == sec_stop,
                    possible_rides
                ))[0]
                ride_length = abs(
                    self.stops.index(last_ride.split('-')[0]) - self.stops.index(last_ride.split('-')[1])
                )

                steps.append({last_ride: ride_length})
                time += self.durations[last_ride]
                stop_one = last_ride.split('-')[index]
                continue

            if stop_one == first_stop and possible_rides == []:
                return (False, first_stop, sec_stop, 0, 0, None)

            for ride in possible_rides:
                indexes = list(map(lambda x: self.stops.index(x),
                                   ride.split('-')))
                ride_length = abs(indexes[0] - indexes[1])
                formatted_rides.append({ride: ride_length})

            formatted_rides = sorted(formatted_rides,
                                     key=lambda x: list(x.values())[0],
                                     reverse=True)

            best_ride = self.select_itinerary(formatted_rides, reversed)

            if best_ride is None:
                index = 0 if reversed is True else 1
                last_stop = list(
                    formatted_rides[0].keys())[0].split('-')[index]

                if '{}-{}'.format(first_stop, last_stop) in direct_itineraries:
                    time = self.durations['{}-{}'.format(first_stop,
                                                         last_stop)]
                    return False, first_stop, sec_stop, 0, time, last_stop

                else:
                    last_ride = list(formatted_rides[0].keys())[0]
                    time += self.durations[last_ride]
                    nb_stops = len(steps)
                    return (False, first_stop, sec_stop, nb_stops, time,
                            last_stop)

            else:
                index = 0 if reversed is True else 1
                stop_one = list(best_ride.keys())[0].split('-')[index]
                time += self.durations[list(best_ride.keys())[0]]
                steps.append(best_ride)

        return True, first_stop, sec_stop, (len(steps) - 1), time, None

    def select_itinerary(self, itineraries, reversed):
        for itinerary in itineraries:
            stops = list(itinerary.keys())[0].split('-')
            index_itinerary = 0 if reversed is True else 1
            index_next = 1 if reversed is True else 0
            next_ride = list(filter(
                lambda x: x[index_next] == stops[index_itinerary],
                list(map(lambda x: x.split('-'), list(self.durations.keys())))
            ))
            if len(next_ride) > 0:
                return itinerary
