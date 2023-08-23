class Flight:
    def __init__(self, flight_id, source, destination,price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price=price
        

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        return [flight for flight in self.flights if flight.flight_id == flight_id]

    def search_by_source(self, source):
        return [flight for flight in self.flights if flight.source.lower() == source.lower()]

    def search_by_destination(self, destination):
        return [flight for flight in self.flights if flight.destination.lower() == destination.lower()]

# Sample flight data
flight_data = [
    ("AI161E90 ", "BLR", "BOM", "5600"),
    ("BR161F91 ", "BOM", "BBI", "6750"),
    ("AI161F99", "BBI", "BLR", "8210"),
    ("VS171E20  ", "JLR", "BBI", "5500"),
    ("AS171G30 ", "HYD", "JLR", "4400"),
    ("AI131F49  ", "HYD", "BOM", "3499"),
    # ... Add more flights
]

# Creating Flight objects and adding them to the database
database = FlightDatabase()
for data in flight_data:
    flight = Flight(*data)
    database.add_flight(flight)

# User input and searching
user_input = input("Enter Flight ID, FROM, TO: ")

found_flights = (
    database.search_by_flight_id(user_input) +
    database.search_by_source(user_input) +
    database.search_by_destination(user_input)
)

# Printing the results
if found_flights:
    for flight in found_flights:
        print("Flight ID:", flight.flight_id)
        print("Source:", flight.source)
        print("Destination:", flight.destination)
        print("Price:", flight.price)
        
        print("-" * 30)
else:
    print("No flights found matching the given input.")
