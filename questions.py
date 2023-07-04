from util import GTFS

class Questions:

    def __init__(self) -> None:
        self.network = GTFS('anaheim')
        self.total = 12

    def solve(self, i: int) -> None:
        if 1 <= i <= self.total:
            getattr(self, f'question_{i}')()
        else:
            raise ValueError(f'Question {i} does not exist.')
    
    def solve_all(self) -> None:
        for i in range(1, self.total + 1):
            print("=" * 20)
            print("Question", i, "\n")
            self.solve(i)

    def question_1(self) -> None:
        """
        Print total number of trips, routes, stops in the network
        """
        print('Total number of trips:', len(self.network.trips))
        print('Total number of routes:', len(self.network.routes))
        print('Total number of stops:', len(self.network.stops))

    def question_2(self) -> None:
        """
        Print the number of trips passing through the Route ID bc404235-c139-4efb-90fb-798fbbddc35c
        """
        print('Number of trips passing through route bc404235-c139-4efb-90fb-798fbbddc35c:', len(self.network.get_trips_by_route('bc404235-c139-4efb-90fb-798fbbddc35c')))

    def question_3(self) -> None:
        """
        Print all trips Id passing through stop id 5011
        """
        print('Trips passing through stop 5011:')
        print(*[stop['trip_id'] for stop in self.network.filter_stop_times(stop_id='5011')], sep='\n')

    def question_4(self) -> None:
        """
        Print the route Id of the trip 689d9098-2132-469c-a01e-a2b90aa70802:1
        """
        print('Route of trip 689d9098-2132-469c-a01e-a2b90aa70802:1:', self.network.get_trip_by_id('689d9098-2132-469c-a01e-a2b90aa70802:1')['route_id'])

    def question_5(self) -> None:
        """
        Can I walk between the stops 63 and 41 ? If yes, what is travel time?
        """
        print('ERROR: Given Stop IDs do not exist!')

    def question_6(self) -> None:
        """
        What is the arrival time of trip 689d9098-2132-469c-a01e-a2b90aa70802:1 on stop Id 6018?
        """
        stoppage = self.network.filter_stop_times(stop_id='6018', trip_id='689d9098-2132-469c-a01e-a2b90aa70802:1')[0]
        print('Arrival time of trip 689d9098-2132-469c-a01e-a2b90aa70802:1 at stop 6018:', stoppage['arrival_time'])

    def question_7(self) -> None:
        """
        What is the number of stop Id 2004 in trip 17e9310e-60b3-4877-8da1-5ce56031f895:1?
        """
        print('Number of stop 2004 in trip 17e9310e-60b3-4877-8da1-5ce56031f895:1:', self.network.filter_stop_times(stop_id='2004', trip_id='17e9310e-60b3-4877-8da1-5ce56031f895:1')[0]['stop_sequence'])

    def question_8(self) -> None:
        """
        What are the stops in the trip 17e9310e-60b3-4877-8da1-5ce56031f895:6 (in the correct order).
        """
        stoppages = self.network.filter_stop_times(trip_id='17e9310e-60b3-4877-8da1-5ce56031f895:6')
        stops = [(stoppage['stop_id'], stoppage['stop_sequence']) for stoppage in stoppages]
        stops.sort(key=lambda x: x[1])
        print('Stops in trip 17e9310e-60b3-4877-8da1-5ce56031f895:6:')
        print(*[s[0] for s in stops], sep='\n')

    def question_9(self) -> None:
        """
        Is arrival time always equal to departure time in all cases?
        """
        for st in self.network.stop_times:
            if st['arrival_time'] != st['departure_time']:
                return print("No, there are stoppages with different arrival and departure times.")
        print("Yes, all stoppages have the same arrival and departure times.")

    def question_10(self) -> None:
        """
        When does the trip 689d9098-2132-469c-a01e-a2b90aa70802:1 depart from stop id 6018?
        """
        stoppage = self.network.filter_stop_times(stop_id='6018', trip_id='689d9098-2132-469c-a01e-a2b90aa70802:1')[0]
        print('Departure time of trip 689d9098-2132-469c-a01e-a2b90aa70802:1 from stop 6018:', stoppage['departure_time'])

    def question_11(self) -> None:
        """
        Is the service_id 02d8b020-a7c1-4ded-a15f-2cab457c9084 active on date 20201225?
        """
        service = self.network.get_service_by_id('02d8b020-a7c1-4ded-a15f-2cab457c9084')
        if service['start_date'] <= '20201225' <= service['end_date']:
            print('Yes, the service is active on 20201225.')
        else:
            print('No, the service is not active on 20201225.')


    def question_12(self) -> None:
        """
        Does the service 022f4234-a772-40d2-a0e4-c9be588a46f9 work on Firday? How many trips does it have?
        """
        service = self.network.get_service_by_id('022f4234-a772-40d2-a0e4-c9be588a46f9')
        if service['friday'] == '1':
            print('Yes, the service works on Friday.')
        else:
            print('No, the service does not work on Friday.')
        print('Number of trips in the service:', len(self.network.get_trips_by_service('022f4234-a772-40d2-a0e4-c9be588a46f9')))
        
