import csv

class GTFS: 

    def __init__(self, network: str) -> None:
        files = ['agency', 'calendar', 'calendar_dates', 'routes', 'shapes', 'stop_times', 'stops', 'transfers', 'trips']
        for f in files:
            setattr(self, f, self.read(f'{network}/{f}.txt'))

    def read(self, filename: str) -> list:
        r = csv.reader(open(filename))
        head = next(r)
        return [dict(zip(head, row)) for row in r]

    def get_trips_by_route(self, route_id: str) -> list:
        return [trip for trip in self.trips if trip['route_id'] == route_id]
    
    def get_trips_by_service(self, service_id: str) -> list:
        return [trip for trip in self.trips if trip['service_id'] == service_id]
    
    def get_trip_by_id(self, trip_id: str) -> dict:
        return [trip for trip in self.trips if trip['trip_id'] == trip_id][0]
    
    def get_stop_by_id(self, stop_id: str) -> dict:
        return [stop for stop in self.stops if stop['stop_id'] == stop_id][0]
    
    def get_service_by_id(self, service_id: str) -> dict:
        return [service for service in self.calendar if service['service_id'] == service_id][0]
    
    def filter_stop_times(self, stop_id: str = None, trip_id: str = None) -> list:
        if stop_id and trip_id:
            return [stop for stop in self.stop_times if stop['stop_id'] == stop_id and stop['trip_id'] == trip_id]
        elif stop_id:
            return [stop for stop in self.stop_times if stop['stop_id'] == stop_id]
        elif trip_id:
            return [stop for stop in self.stop_times if stop['trip_id'] == trip_id]
