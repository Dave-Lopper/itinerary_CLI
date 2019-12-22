class Calculator():
    def __init__(self, stops, durations):
        self.stops = stops
        self.durations = durations

    def calculate(self, first_stop, last_stop):
        journey_length = abs(self.stops.index(
            first_stop) - self.stops.index(last_stop))
        formatted_journey = sorted([first_stop, last_stop])
        formatted_string = '{}-{}'.format(formatted_journey[0],
                                          formatted_journey[1])
        direct_itineraries = list(self.durations.keys())
        reversed = False
        if (self.stops.index(first_stop) > self.stops.index(last_stop)):
            reversed = True

        if journey_length == 1:
            if formatted_string in direct_itineraries:
                nb_stops = 0
                time = self.durations[formatted_string]
                return True, first_stop, last_stop, 0, time, None
            else:
                return False, first_stop, last_stop, 0, 0, None

        stop_one = first_stop
        time = 0
        steps = []
        index_ride_departure = 1 if reversed is True else 0
        index_ride_arrival = 0 if reversed is True else 1

        while stop_one != last_stop:
            possible_rides = list(filter(
                lambda x: stop_one == x.split('-')[index_ride_departure],
                direct_itineraries
            ))
            formatted_rides = []

            if stop_one == first_stop and possible_rides == []:
                return False, first_stop, last_stop, 0, 0, None

            for ride in possible_rides:
                indexes = list(map(lambda x: self.stops.index(x),
                                   ride.split('-')))
                ride_length = abs(indexes[0] - indexes[1])

                if ride.split('-')[index_ride_arrival] == last_stop:
                    steps.append({ride: ride_length})
                    time += self.durations[ride]
                    stop_one = ride.split('-')[index_ride_arrival]
                    break
                formatted_rides.append({ride: ride_length})

            if last_stop == stop_one:
                continue

            formatted_rides = sorted(formatted_rides,
                                     key=lambda x: list(x.values())[0],
                                     reverse=True)

            best_ride = self.select_itinerary(formatted_rides, reversed)

            if best_ride is None:
                final_stop = list(
                    formatted_rides[0].keys())[0].split('-')[index_ride_arrival]

                if '{}-{}'.format(first_stop, final_stop) in direct_itineraries:
                    time = self.durations['{}-{}'.format(first_stop,
                                                         final_stop)]
                    return False, first_stop, last_stop, 0, time, final_stop

                else:
                    last_ride = list(formatted_rides[0].keys())[0]
                    time += self.durations[last_ride]
                    nb_stops = len(steps)
                    return (False, first_stop, last_stop, nb_stops, time,
                            final_stop)

            else:
                stop_one = list(best_ride.keys())[0].split('-')[index_ride_arrival]
                time += self.durations[list(best_ride.keys())[0]]
                steps.append(best_ride)

        return True, first_stop, last_stop, (len(steps) - 1), time, None

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
