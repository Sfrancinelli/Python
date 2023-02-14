class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.iataCode = None

    def get_iata_code(self, city):
        if city != '':
            self.iataCode = "TESTING"
            return self.iataCode
